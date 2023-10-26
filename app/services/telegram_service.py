from app.services.bots.telegram_bot import TelegramBot
from io import BytesIO
from telegram import Message, InputMediaPhoto


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
        media_group: list[InputMediaPhoto],
        *args,
        **kwargs
    ) -> tuple[Message]:
        """
        Post image to telegram channel

        Args:
            telegram_bot (TelegramBot): telegram bot entity
            channel_id (str): telegram channel id to post to
            images (list[InputMediaPhoto]): list of InputMediaPhoto objects

        Returns:
            messages (tuple[Message]): tuple of telegram objects Message which represent posted messages to telegram chat
        """

        return await telegram_bot.bot.send_media_group(
            chat_id=channel_id, media=media_group, *args, **kwargs
        )
