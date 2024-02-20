import asyncio

from .oenp_bot import OENPBot
from infrastructure.config import Config
from infrastructure.logging import set_logging


def run_bot():
    set_logging()
    bot = OENPBot(
        Config.TELEGRAM_BOT_TOKEN,
        Config.OENP_API_URL,
        Config.OEIS_API_URL,
    )

    asyncio.run(bot.run())


if __name__ == "__main__":
    run_bot()
