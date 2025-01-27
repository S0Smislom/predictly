from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from app_prediction.models import (
    AudioPrediction,
    ImagePrediction,
    TextPrediction,
    VideoPrediction,
)
from app_prediction.services import PredictionService
from bot.common.template import welcome_message
from bot.utils.chat import no_predictions_error, save_chat
from bot.utils.prediction import (
    handle_audio_prediction,
    handle_image_prediction,
    handle_text_prediction,
    handle_video_prediction,
)

main_router = Router()


@main_router.message(CommandStart())
async def start_handler(message: Message):
    _ = await save_chat(message)
    await message.answer(text=welcome_message.render())


@main_router.message(Command("predict"))
async def predict_handler(message: Message):
    chat, current_user = await save_chat(message)

    prediction = await PredictionService().get_random()
    if not prediction:
        return await no_predictions_error(message)

    prediction_object = await prediction.aget_content_object()
    if not prediction_object:
        return await no_predictions_error(message)
    chat_users = [_ async for _ in chat.users.all()]
    if isinstance(prediction_object, TextPrediction):
        return await handle_text_prediction(
            message, prediction_object, current_user, chat_users
        )

    if isinstance(prediction_object, AudioPrediction):
        return await handle_audio_prediction(message, prediction_object)

    if isinstance(prediction_object, VideoPrediction):
        return await handle_video_prediction(message, prediction_object)

    if isinstance(prediction_object, ImagePrediction):
        return await handle_image_prediction(message, prediction_object)

    return await no_predictions_error(message)
