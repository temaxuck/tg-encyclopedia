from app.services.bots.telegram_bot import TelegramBot
from app.services.api_service import OENPService, OEISService
from app.services.bots.oenp_bot.handlers import search, pyramids, common, COMMANDS
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage


class OENPBot(TelegramBot):
    """
    Online Encyclopedia of Number Pyramids Telegram Bot

    This bot is intended to interact with user
    """

    telegram_post_format = {
        "font_size": 20,
        "padding": 40,
    }

    def __init__(
        self,
        bot_token: str,
        oenp_api_url: str,
        oeis_api_url: str,
        telegram_post_format: dict = None,
    ) -> None:
        """Initialize bot

        Args:
            bot_token (str): API token recieved from @BotFather
            oenp_api_url (str): URL to Online Encyclopedia of Number Pyramids API
            oeis_api_url (str): URL to On-Line Encyclopedia of Integer Sequences API
            telegram_post_format (dict): Dictionary object that should contain "font_size" and "padding" keys,
                where "font_size" key is the size (in px) of font of latex symbols in image
                and "padding" key is the size (in px) of padding of latex expression within image
        """
        self.bot = Bot(token=bot_token)
        self.dp = Dispatcher(storage=MemoryStorage())
        self.oenp_service = OENPService(oenp_api_url)  # to be removed
        self.oeis_service = OEISService(oeis_api_url)  # to be removed

        if telegram_post_format is not None:
            self.telegram_post_format = telegram_post_format

        self.dp.include_router(router=common.router)
        self.dp.include_router(router=pyramids.router)
        self.dp.include_router(router=search.router)

    async def set_menu(self):
        main_menu_commands = [
            BotCommand(command=command, description=description)
            for command, description in COMMANDS.items()
        ]
        await self.bot.set_my_commands(main_menu_commands)

    async def run(self):
        await self.set_menu()
        await self.dp.start_polling(self.bot)
