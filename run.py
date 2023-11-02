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
        telegram_post_format=Config.TELEGRAM_POST_FORMAT,
    )

    async def load_batches():
        await bot.post_pyramids_to_channel(range(1, 10), latency=60)
        await bot.post_pyramid_to_channel(484)
        await bot.post_pyramid_to_channel(range(600, 620), latency=60)
        await bot.post_pyramid_to_channel(range(1000, 1020), latency=60)
        await bot.post_pyramid_to_channel(range(1450, 1500), latency=60)

    asyncio.run(load_batches())


run_bot()
