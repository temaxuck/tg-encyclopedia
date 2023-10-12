import asyncio
from app.services.bots.telegram_bot import TelegramBot


class TelegramService:
    """
    Telegram service to communicate with telegram api
    """

    @staticmethod
    def post_message_to_channel(
        telegram_bot: TelegramBot, channel_id: str, text: str
    ) -> None:
        """Post message to the telegram channel

        Args:
            telegram_bot (TelegramBot): telegram bot entity
            channel_id (str): telegram channel id
            text (str): text message to post
        """

        asyncio.run(telegram_bot.bot.send_message(chat_id=channel_id, text=text))
