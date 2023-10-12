from app.services.telegram_service import TelegramService
from app.services.bots.telegram_bot import TelegramBot
from telegram import Bot
from io import BytesIO
from PIL import Image


class OENPBot(TelegramBot):
    """
    Online Encyclopedia of Number Pyramids Telegram Bot

    This bot is intended to post messages to
    Online Encyclopedia of Number Pyramids telegram channel
    """

    def __init__(self, bot_token: str, channel_id: str) -> None:
        """Initialize bot

        Args:
            bot_token (str): API token recieved from @BotFather
            channel_id (str): Telegram channel id to which this bot is going to post messages
        """
        self.bot = Bot(token=bot_token)  # Initializing telegram bot
        self.channel_id = channel_id

    def post_message_to_channel(self, text: str) -> None:
        """Post message to telegram channel

        Args:
            text (str): text message to post
        """

        TelegramService.post_message_to_channel(self, self.channel_id, text)

    def post_image_to_channel(self, image_bytes: BytesIO, caption: str) -> None:
        """
        Post image to telegram channel

        Args:
            image_bytes (BytesIO): image represented by BytesIO object
            text (str): text message to post
        """
        image = Image.open(image_bytes)

        byte_arr = BytesIO()
        image.save(byte_arr, format="PNG")

        byte_arr.seek(0)

        TelegramService.post_image_to_channel(self, self.channel_id, byte_arr, caption)
