# To be moved to CLI
import asyncio

from .oenp_channel_bot import OENPChannelBot
from infrastructure.config import Config
from infrastructure.logging import set_logging
from infrastructure.argparse import get_arg_parser


def load_pyarmids_to_channel():
    parser = get_arg_parser()
    args = parser.parse_args()

    set_logging(args.log_level)

    bot = OENPChannelBot(
        bot_token=Config.TELEGRAM_BOT_TOKEN,
        channel_id=Config.TELEGRAM_CHANNEL_ID,
        oenp_api_url=Config.OENP_API_URL,
        oeis_api_url="https://oeis.org/",
        telegram_post_format=Config.TELEGRAM_POST_FORMAT,
    )

    asyncio.run(
        bot.post_pyramids_to_channel(
            range(args.start, args.end),
            latency=args.latency,
        )
    )
    # async def load_batches():
    #     await bot.post_pyramids_to_channel(range(600, 620), latency=args.latency)
    #     await bot.post_pyramids_to_channel(range(1000, 1020), latency=args.latency)
    #     await bot.post_pyramids_to_channel(range(1450, 1500), latency=args.latency)

    # if not (start and end):
    #     asyncio.run(load_batches())
    # else:


if __name__ == "__main__":
    load_pyarmids_to_channel()
