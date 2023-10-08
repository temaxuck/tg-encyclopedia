import logging
from domain.telegram.bot import OENPBot
from infrastructure.config import Config

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def run_bot():
    bot = OENPBot(
        bot_token=Config.TELEGRAM_BOT_TOKEN, channel_id=Config.TELEGRAM_CHANNEL_ID
    )

    bot.post_message_to_channel(text="Test message")


run_bot()
