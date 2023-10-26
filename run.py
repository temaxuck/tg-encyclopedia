from app.services.bots.oenp_bot import OENPBot
from infrastructure.config import Config
from infrastructure.logging import set_logging
import asyncio


def run_bot():
    set_logging()

    bot = OENPBot(
        bot_token=Config.TELEGRAM_BOT_TOKEN,
        channel_id=Config.TELEGRAM_CHANNEL_ID,
        oenp_api_url=Config.OENP_API_URL,
        oeis_api_url="https://oeis.org/",
    )

    asyncio.run(bot.post_pyramids_to_channel(range(1, 2000), latency=60))


run_bot()
