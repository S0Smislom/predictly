from bot.app import TelegramBot
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Starts tg bot"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("Run bot")
        TelegramBot().run()
