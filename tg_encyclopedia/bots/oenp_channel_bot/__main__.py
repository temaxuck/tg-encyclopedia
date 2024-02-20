# To be moved to CLI
import asyncio

from infrastructure.config import Config
from infrastructure.logging import set_logging
from tg_encyclopedia.bots.oenp_channel_bot import OENPChannelBot


def load_pyarmids_to_channel(start: int = None, end: int = None, latency: int = 60):
    set_logging()

    bot = OENPChannelBot(
        bot_token=Config.TELEGRAM_BOT_TOKEN,
        channel_id=Config.TELEGRAM_CHANNEL_ID,
        oenp_api_url=Config.OENP_API_URL,
        oeis_api_url="https://oeis.org/",
        telegram_post_format=Config.TELEGRAM_POST_FORMAT,
    )

    async def load_batches():
        await bot.post_pyramids_to_channel(range(600, 620), latency=latency)
        await bot.post_pyramids_to_channel(range(1000, 1020), latency=latency)
        await bot.post_pyramids_to_channel(range(1450, 1500), latency=latency)

    if not (start and end):
        asyncio.run(load_batches())
    else:
        asyncio.run(bot.post_pyramids_to_channel(range(start, end), latency=latency))


if __name__ == "__main__":
    load_pyarmids_to_channel()
