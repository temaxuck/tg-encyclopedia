import logging
from domain.telegram.bot import OENPBot
from infrastructure.config import Config
from infrastructure.utils import convert_latex_to_image

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def run_bot():
    bot = OENPBot(
        bot_token=Config.TELEGRAM_BOT_TOKEN, channel_id=Config.TELEGRAM_CHANNEL_ID
    )

    latex_expr = r"U_{1}(x, y) = x + y \\ \delta{(a, b)} = \begin{cases}1&\text{if a = b},\\ 0  \end{cases} \\ T_{1}(n, m, k) = \delta{\left(k,m + n \right)} {\binom{m + n}{m}}"

    # bot.post_message_to_channel(text="Test message")
    image_bytes = convert_latex_to_image(latex_expr)

    from PIL import Image
    import io

    # Assuming 'bytes_io' is your BytesIO object
    bytes_io = io.BytesIO()

    # To save the BytesIO object as an image
    bytes_io.seek(0)
    img = Image.open(image_bytes)
    img.save("output.png")


run_bot()
