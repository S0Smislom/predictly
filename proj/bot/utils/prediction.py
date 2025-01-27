from random import choice, randint
from typing import List

from aiogram.types import BufferedInputFile, Message
from app_bot.models import User
from app_prediction.models import (
    AudioPrediction,
    ImagePrediction,
    TextPrediction,
    VideoPrediction,
)
from jinja2 import Template


def create_text_template(prediction_object: TextPrediction):
    template = Template(prediction_object.text)
    template.globals.update(
        username=lambda users: f"@{choice(users).username}",
    )
    return template


async def handle_text_prediction(
    message: Message,
    prediction_object: TextPrediction,
    current_user: User,
    chat_users: List[User],
):
    template = create_text_template(prediction_object)
    rendered_text = template.render(current_user=current_user, users=chat_users)
    return await message.answer(
        text=rendered_text, reply_to_message_id=message.message_id
    )


async def handle_audio_prediction(message: Message, prediction_object: AudioPrediction):
    return await message.answer_voice(
        voice=BufferedInputFile(
            file=prediction_object.file.read(),
            filename=prediction_object.file.name,
        ),
        caption=prediction_object.get_caption(),
        reply_to_message_id=message.message_id,
    )


async def handle_video_prediction(message: Message, prediction_object: VideoPrediction):

    return await message.answer_video(
        video=BufferedInputFile(
            file=prediction_object.file.read(),
            filename=prediction_object.file.name,
        ),
        caption=prediction_object.get_caption(),
        reply_to_message_id=message.message_id,
    )


async def handle_image_prediction(message: Message, prediction_object: ImagePrediction):
    return await message.answer_photo(
        photo=BufferedInputFile(
            file=prediction_object.file.read(),
            filename=prediction_object.file.name,
        ),
        caption=prediction_object.get_caption(),
        reply_to_message_id=message.message_id,
    )
