from aiogram.types import Message
from app_bot.services import ChatService, UserService


async def save_chat(message: Message):
    user, _ = await UserService().get_or_create(
        message.from_user.id, username=message.from_user.username
    )
    chat, _ = await ChatService().get_or_create(message.chat.id, [user])
    return chat


async def no_predictions_error(message: Message) -> Message:
    return await message.answer(text="Сеодня нет предсказаний")
