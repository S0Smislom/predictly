from typing import List, Tuple

from app_bot.models import Chat, User


class ChatService:
    async def get_or_create(self, chat_id, users: List[User]) -> Tuple[Chat, bool]:
        chat, created = await Chat.objects.aget_or_create(id=chat_id)
        await chat.users.aadd(*users)
        return chat, created
