from aiogram import Bot
from aiogram.client.bot import DefaultBotProperties
from django.conf import settings

bot = Bot(settings.TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode="html"))
