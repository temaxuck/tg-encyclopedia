from app.services.bots.oenp_bot import OENPBot
from infrastructure.config import Config
from infrastructure.logging import set_logging
import asyncio


def run_bot():
    set_logging()

    bot = OENPBot(
        bot_token=Config.TELEGRAM_BOT_TOKEN,
        channel_id=Config.TELEGRAM_CHANNEL_ID,
        api_url=Config.OENP_API_URL,
    )

    asyncio.run(bot.post_pyramids_to_channel(range(20, 60), latency=1))


run_bot()
