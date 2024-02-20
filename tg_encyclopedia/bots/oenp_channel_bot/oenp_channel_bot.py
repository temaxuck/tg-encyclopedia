import time

from io import BytesIO
from telegram import Bot, Message, InputMediaPhoto
from telegram.constants import ParseMode
from typing import List, Tuple


from infrastructure.logging import log_telegram_error
from tg_encyclopedia.bots.telegram_bot import TelegramBot
from tg_encyclopedia.services.telegram_service import TelegramService
from tg_encyclopedia.services.api_service import OENPService, OEISService
from infrastructure.utils import (
    convert_latex_to_image,
    get_formatted_gf_latex,
)


class OENPChannelBot(TelegramBot):
    """
    Online Encyclopedia of Number Pyramids Telegram Bot

    This bot is intended to post messages to
    Online Encyclopedia of Number Pyramids telegram channel
    """

    telegram_post_format = {
        "font_size": 20,
        "padding": 40,
    }

    def __init__(
        self,
        bot_token: str,
        channel_id: str,
        oenp_api_url: str,
        oeis_api_url: str,
        telegram_post_format: dict = None,
    ) -> None:
        """Initialize bot

        Args:
            bot_token (str): API token recieved from @BotFather
            channel_id (str): Telegram channel id to which this bot is going to post messages
            oenp_api_url (str): URL to Online Encyclopedia of Number Pyramids API
            oeis_api_url (str): URL to On-Line Encyclopedia of Integer Sequences API
            telegram_post_format (dict): Dictionary object that should contain "font_size" and "padding" keys,
                where "font_size" key is the size (in px) of font of latex symbols in image
                and "padding" key is the size (in px) of padding of latex expression within image
        """
        self.bot = Bot(token=bot_token)  # Initializing telegram bot
        self.oenp_service = OENPService(oenp_api_url)
        self.oeis_service = OEISService(oeis_api_url)
        self.channel_id = channel_id

        if telegram_post_format is not None:
            self.telegram_post_format = telegram_post_format

    @log_telegram_error
    async def post_message_to_channel(
        self,
        text: str,
        parse_mode: ParseMode = ParseMode.HTML,
        *args,
        **kwargs,
    ) -> Message:
        """Post message to telegram channel

        Args:
            text (str): text message to post
            parse_mode <Optional> (ParseMode): text's parse_mode, by default ParseMode.HTML

        Returns:
            message (Message): telegram object Message which represents posted message to telegram chat
        """

        return await TelegramService.post_message_to_channel(
            self,
            self.channel_id,
            text,
            parse_mode=parse_mode,
            *args,
            **kwargs,
        )

    @log_telegram_error
    async def post_image_to_channel(
        self,
        image_bytes: BytesIO,
        parse_mode: ParseMode = ParseMode.HTML,
        *args,
        **kwargs,
    ) -> Message:
        """
        Post image to telegram channel

        Args:
            image_bytes (BytesIO): image represented by BytesIO object
            parse_mode <Optional> (ParseMode): caption's parse_mode, by default ParseMode.HTML

        Returns:
            message (Message): telegram object Message which represents posted message to telegram chat
        """

        return await TelegramService.post_image_to_channel(
            self,
            self.channel_id,
            image_bytes,
            parse_mode=parse_mode,
            *args,
            **kwargs,
        )

    @log_telegram_error
    async def post_images_to_channel(
        self,
        images: List[BytesIO],
        caption: str = None,
        parse_mode: ParseMode = ParseMode.HTML,
        *args,
        **kwargs,
    ) -> Tuple[Message]:
        """
        Post image to telegram channel

        Args:
            images (List[BytesIO]): List of images represented by BytesIO objects
            caption <Optional> (str): caption describing images
            parse_mode <Optional> (ParseMode): caption's parse_mode, by default ParseMode.HTML

        Returns:
            messages (Tuple[Message]): Tuple of telegram objects Message which represent posted messages to telegram chat
        """
        media_group = [
            InputMediaPhoto(
                image,
                caption=caption if index == 0 else "",
                parse_mode=parse_mode,
            )
            for index, image in enumerate(images)
        ]

        return await TelegramService.post_images_to_channel(
            self,
            self.channel_id,
            media_group,
            *args,
            **kwargs,
        )

    @log_telegram_error
    async def post_pyramid_to_channel(self, sequence_number: int) -> Message:
        """
        Post pyramid object to telegram channel

        Args:
            sequence_number (int): Pyramid's sequence number by encyclopedia https://oenp.tusur.ru/

        Returns:
            Message:  telegram objects Message which represent posted message to telegram chat

        """
        pyramid = self.oenp_service.get_pyramid_by_sequence_number(
            sequence_number=sequence_number
        )
        oeis_response, oeis_url = self.oeis_service.get_sequence_by_data(
            pyramid["data"]
        )

        oeis_reference_str = (
            f"\nOEIS reference: {oeis_url}"
            if oeis_response["results"] is not None
            else "\nNo OEIS reference"
        )
        caption = f"Pyramid #{pyramid['sequence_number']}." + oeis_reference_str

        gf_latex = pyramid["gf_latex"].replace("$", "")
        image = convert_latex_to_image(
            get_formatted_gf_latex(gf_latex),
            font_size=self.telegram_post_format["font_size"],
            padding=self.telegram_post_format["padding"],
        )

        return await self.post_image_to_channel(
            image_bytes=image,
            caption=caption,
        )

    async def post_pyramids_to_channel(
        self, snid_range: range, latency: float = 60
    ) -> List[Tuple[Message]]:
        """
        Post pyramid objects to telegram channel in provided range

        Args:
            snid_range (range): range of Pyramid's sequence numbers according to encyclopedia https://oenp.tusur.ru/
            latency (float): latency (in seconds) between posting each pyramid, by default 60 second

        Returns:
            Tuple[Tuple[Message]]: List of Tuples of telegram objects Message which represent posted messages

                *As we post one pyramid object in 3 messages (posting Generating function, Explicit formula, Data),
                 which are being put in one Tuple, when we post multiple pyramids, we put these Tuples in List
        """
        messages = []

        for i in snid_range:
            messages.append(await self.post_pyramid_to_channel(i))
            print(f"Done: {i-snid_range.start+1}/{snid_range.stop-snid_range.start}")
            time.sleep(latency)

        return messages
