from telegram import Bot
import asyncio


class OENPBot:
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
        """Post message to the telegram channel

        Args:
            text (str): text message to post
        """

        asyncio.run(self.bot.send_message(chat_id=self.channel_id, text=text))
