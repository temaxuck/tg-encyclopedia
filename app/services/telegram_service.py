from io import BytesIO
from telegram import Message, InputMediaPhoto
from typing import List, Tuple

from app.services.bots.telegram_bot import TelegramBot

class TelegramService:
    """
    Telegram service to communicate with telegram api
    """

    @staticmethod
    async def post_message_to_channel(
        telegram_bot: TelegramBot, channel_id: str, text: str, *args, **kwargs
    ) -> Message:
        """Post message to the telegram channel

        Args:
            telegram_bot (TelegramBot): telegram bot entity
            channel_id (str): telegram channel id to post to
            text (str): text message to post

        Returns:
            message (Message): telegram object Message which represents posted message to telegram chat
        """

        return await telegram_bot.bot.send_message(
            chat_id=channel_id, text=text, *args, **kwargs
        )

    @staticmethod
    async def post_image_to_channel(
        telegram_bot: TelegramBot, channel_id: str, image: BytesIO, *args, **kwargs
    ) -> Message:
        """Post message to the telegram channel

        Args:
            telegram_bot (TelegramBot): telegram bot entity
            channel_id (str): telegram channel id to post to
            image (BytesIO): image represented in BytesIO object

        Returns:
            message (Message): telegram object Message which represents posted message to telegram chat
        """

        return await telegram_bot.bot.send_photo(
            chat_id=channel_id, photo=image, *args, **kwargs
        )

    @staticmethod
    async def post_images_to_channel(
        telegram_bot: TelegramBot,
        channel_id: str,
        media_group: List[InputMediaPhoto],
        *args,
        **kwargs
    ) -> Tuple[Message]:
        """
        Post image to telegram channel

        Args:
            telegram_bot (TelegramBot): telegram bot entity
            channel_id (str): telegram channel id to post to
            images (List[InputMediaPhoto]): List of InputMediaPhoto objects

        Returns:
            messages (Tuple[Message]): Tuple of telegram objects Message which represent posted messages to telegram chat
        """

        return await telegram_bot.bot.send_media_group(
            chat_id=channel_id, media=media_group, *args, **kwargs
        )
