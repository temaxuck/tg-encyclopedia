from app.services.bots.telegram_bot import TelegramBot
from io import BytesIO
from telegram.constants import ParseMode
from telegram import Message


class TelegramService:
    """
    Telegram service to communicate with telegram api
    """

    @staticmethod
    async def post_message_to_channel(
        telegram_bot: TelegramBot,
        channel_id: str,
        text: str,
        reply_to_message_id: int = None,
    ) -> Message:
        """Post message to the telegram channel

        Args:
            telegram_bot (TelegramBot): telegram bot entity
            channel_id (str): telegram channel id
            text (str): text message to post
            reply_to_message_id <Optional> (int): message id to reply
        """

        return await telegram_bot.bot.send_message(
            chat_id=channel_id, text=text, reply_to_message_id=reply_to_message_id
        )

    @staticmethod
    async def post_image_to_channel(
        telegram_bot: TelegramBot,
        channel_id: str,
        image: BytesIO,
        caption: str = None,
        parse_mode: ParseMode = ParseMode.HTML,
    ) -> Message:
        """Post message to the telegram channel

        Args:
            telegram_bot (TelegramBot): telegram bot entity
            channel_id (str): telegram channel id
            image (BytesIO): image represented in BytesIO object
            caption <Optional> (str): text going along with provided image
            parse_mode <Optional> (ParseMode): caption's parse_mode, by default ParseMode.HTML
        """

        return await telegram_bot.bot.send_photo(
            chat_id=channel_id, photo=image, caption=caption, parse_mode=parse_mode
        )
