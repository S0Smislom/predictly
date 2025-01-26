from typing import Tuple

from app_bot.models import User


class UserService:
    async def get_or_create(
        self, user_id, username: str, **kwargs
    ) -> Tuple[User, bool]:
        user, created = await User.objects.aget_or_create(id=user_id)
        if not user.username:
            user.username = username
            await user.asave()
        return user, created
