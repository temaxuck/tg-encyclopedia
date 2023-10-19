import asyncio
from app.services.bots.telegram_bot import TelegramBot
from io import BytesIO
from telegram.constants import ParseMode


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

    @staticmethod
    def post_image_to_channel(
        telegram_bot: TelegramBot,
        channel_id: str,
        image: BytesIO,
        caption: str,
        parse_mode: ParseMode = ParseMode.HTML,
    ) -> None:
        """Post message to the telegram channel

        Args:
            telegram_bot (TelegramBot): telegram bot entity
            channel_id (str): telegram channel id
            image (BytesIO): image represented in BytesIO object
            caption (str): text going along with provided image
            parse_mode <Optional> (ParseMode): caption's parse_mode, by default ParseMode.HTML
        """

        asyncio.run(
            telegram_bot.bot.send_photo(
                chat_id=channel_id, photo=image, caption=caption, parse_mode=parse_mode
            )
        )
