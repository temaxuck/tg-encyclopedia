from app.services.telegram_service import TelegramService
from app.services.bots.telegram_bot import TelegramBot
from app.services.api_service import OENPService
from infrastructure.utils import (
    convert_latex_to_image,
    get_pyramid_latex_representation,
)
from telegram import Bot, Message
from telegram.constants import ParseMode
from io import BytesIO
from PIL import Image
from html import escape


class OENPBot(TelegramBot):
    """
    Online Encyclopedia of Number Pyramids Telegram Bot

    This bot is intended to post messages to
    Online Encyclopedia of Number Pyramids telegram channel
    """

    def __init__(self, bot_token: str, channel_id: str, api_url: str) -> None:
        """Initialize bot

        Args:
            bot_token (str): API token recieved from @BotFather
            channel_id (str): Telegram channel id to which this bot is going to post messages
            api_url (str): URL to Online Encyclopedia of Number Pyramids API
        """
        self.bot = Bot(token=bot_token)  # Initializing telegram bot
        self.oenp_service = OENPService(api_url)
        self.channel_id = channel_id

    def post_message_to_channel(
        self, text: str, reply_to_message_id: int = None
    ) -> Message:
        """Post message to telegram channel

        Args:
            text (str): text message to post
            reply_to_message_id <Optional> (int): message id to reply
        """

        return TelegramService.post_message_to_channel(
            self, self.channel_id, text, reply_to_message_id=reply_to_message_id
        )

    def post_image_to_channel(
        self,
        image_bytes: BytesIO,
        caption: str = None,
        parse_mode: ParseMode = ParseMode.HTML,
    ) -> Message:
        """
        Post image to telegram channel

        Args:
            image_bytes (BytesIO): image represented by BytesIO object
            caption <Optional> (str): text message to post
            parse_mode <Optional> (ParseMode): caption's parse_mode, by default ParseMode.HTML
        """
        image = Image.open(image_bytes)

        byte_arr = BytesIO()
        image.save(byte_arr, format="PNG")

        byte_arr.seek(0)

        return TelegramService.post_image_to_channel(
            self, self.channel_id, byte_arr, caption=caption, parse_mode=parse_mode
        )

    def post_pyramid_to_channel(self, sequence_number: int) -> list[Message]:
        """
        Post pyramid object to telegram channel

        Args:
            sequence_number (int): Pyramid's sequence number by encyclopedia https://oenp.tusur.ru/
        """
        pyramid = self.oenp_service.get_pyramid_by_sequence_number(
            sequence_number=sequence_number
        )

        gf_latex = pyramid["gf_latex"].replace("$", "")
        ef_latex = pyramid["ef_latex"].replace("$", "")

        latex_expression = get_pyramid_latex_representation(
            pyramid["sequence_number"], gf_latex, ef_latex
        )
        latex_expression_image = convert_latex_to_image(latex_expression)

        latex_representation = "$$" + gf_latex + r" \\ " + ef_latex + "$$"

        caption = (
            f"<b>Pyramid #{pyramid['sequence_number']}</b>"
            "\nPyramid's data table:"
            f"<code>\n{pyramid['data']}</code>"
            "\nPyramid's latex representation:"
            f"<code>\n{escape(latex_representation)}</code>"
        )

        image_message = self.post_image_to_channel(image_bytes=latex_expression_image)
        text_message = self.post_message_to_channel(
            caption, reply_to_message_id=image_message.message_id
        )

        return [image_message, text_message]
