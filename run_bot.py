from infrastructure.config import Config
from infrastructure.logging import set_logging
from app.services.bots.oenp_bot.oenp_bot import OENPBot
import asyncio


async def run_bot():
    bot = OENPBot(
        Config.TELEGRAM_BOT_TOKEN,
        Config.OENP_API_URL,
        Config.OEIS_API_URL,
    )

    await bot.run()


if __name__ == "__main__":
    set_logging()
    asyncio.run(run_bot())
