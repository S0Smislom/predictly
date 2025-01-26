from random import randint

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import BufferedInputFile, Message
from app_prediction.models import (
    AudioPrediction,
    ImagePrediction,
    TextPrediction,
    VideoPrediction,
)
from app_prediction.services import PredictionService
from bot.common.template import welcome_message
from bot.utils.chat import no_predictions_error, save_chat
from jinja2 import Template

main_router = Router()


@main_router.message(CommandStart())
async def start_handler(message: Message):
    _ = await save_chat(message)
    await message.answer(text=welcome_message.render())


@main_router.message(Command("predict"))
async def predict_handler(message: Message):
    chat = await save_chat(message)

    prediction = await PredictionService().get_random()
    if not prediction:
        return await no_predictions_error(message)

    prediction_object = await prediction.aget_content_object()
    if not prediction_object:
        return await no_predictions_error(message)
    chat_users = [_ async for _ in chat.users.all()]

    if isinstance(prediction_object, TextPrediction):
        template = Template(prediction_object.text)
        template.globals.update(
            username=lambda users: "@" + users[randint(0, len(users) - 1)].username,
        )
        return await message.answer(
            text=template.render(users=chat_users),
            reply_to_message_id=message.message_id,
        )
    elif isinstance(prediction_object, AudioPrediction):
        return await message.answer_voice(
            BufferedInputFile(
                file=prediction_object.file.read(),
                filename=prediction_object.file.name,
            ),
            reply_to_message_id=message.message_id,
        )
    elif isinstance(prediction_object, VideoPrediction):
        return await message.answer_video(
            BufferedInputFile(
                file=prediction_object.file.read(),
                filename=prediction_object.file.name,
            ),
            caption="Твое видео сказание",
            reply_to_message_id=message.message_id,
        )
    elif isinstance(prediction_object, ImagePrediction):
        return await message.answer_photo(
            photo=BufferedInputFile(
                file=prediction_object.file.read(),
                filename=prediction_object.file.name,
            ),
            caption="Твое мем сказание",
            reply_to_message_id=message.message_id,
        )

    return await no_predictions_error(message)
