import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseStorage

from .bot import bot
from .routers import main_router


class TelegramBot:

    def __init__(self):
        self.dp = self._get_dispatcher()
        self.bot = self._get_bot()

    def run(self):
        asyncio.run(self.run_async())

    async def run_async(self):
        await self.dp.start_polling(self.bot)

    def _add_handlers(self, dp: Dispatcher):
        dp.include_router(main_router)

    def _add_middlewares(self, dp: Dispatcher):
        pass

    def _get_dispatcher(self) -> Dispatcher:
        storage = self._get_storage()
        dp = Dispatcher(storage=storage)
        self._add_handlers(dp)
        self._add_middlewares(dp)
        return dp

    def _get_storage(self) -> BaseStorage:
        return
        # return RedisStorage.from_url(settings.TELEGRAM_BOT_STORAGE_URL)

    def _get_bot(self):
        return bot
