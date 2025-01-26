from abc import ABC, abstractmethod
from typing import List

from app_bot.models import User


class IPredictionService(ABC):

    @abstractmethod
    async def predict(self, members: List[User]) -> str:
        pass
