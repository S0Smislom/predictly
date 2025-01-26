import json
from json.decoder import JSONDecodeError
from typing import List
from uuid import uuid4

import aiohttp
from app_bot.models import User

from proj.port.prediction import IPredictionService


class GigachatPredictionService(IPredictionService):
    def __init__(self, api_key: str, scope: str = "GIGACHAT_API_PERS"):
        self.GIGACHAT_API_KEY = api_key
        self.SCOPE = scope

    async def predict(self, members: List[User]):
        data = await self._chat(
            f"Можешь использовать одного или несколько человек из списка: [{', '.join([item.username for item in members])}]."
        )
        return self._parse_response(data)

    async def _chat(self, promt: str):
        token = await self._get_token()
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://gigachat.devices.sberbank.ru/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                json={
                    "model": "GigaChat-Max",
                    "messages": [
                        {"role": "system", "content": self._get_system_promt()},
                        {
                            "role": "user",
                            "content": self._get_system_promt() + promt,
                        },
                    ],
                    "stream": False,
                    "update_interval": 0,
                },
                ssl=False,
            ) as response:
                return await response.json()

    async def _get_token(self):
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
        headers = {
            "Authorization": f"Bearer {self.GIGACHAT_API_KEY}",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "RqUID": str(uuid4()),
        }
        data = {"scope": self.SCOPE}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, headers=headers, data=data, ssl=False
            ) as response:
                data = await response.json()
            return data.get("access_token")

    def _get_system_promt(self) -> str:
        return f'Ты гадалка в 5 поколении. Сделай забавное предсказание на сегодня. Верни ответ в виде json {{"prediction": ""}}'

    def _parse_response(self, data: dict):
        content = data["choices"][0]["message"]["content"]
        if not content:
            raise Exception("Не смог получить предсказания")
        try:
            data = json.loads(content)
        except JSONDecodeError:
            raise Exception("Не смог получить предсказания")
        try:
            return data["prediction"]
        except KeyError:
            raise Exception("Не смог получить предсказания")
