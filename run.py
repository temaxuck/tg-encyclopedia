import logging
from app.services.bots.oenp_bot import OENPBot
from infrastructure.config import Config
from infrastructure.utils import convert_latex_to_image
from app.services.api_service import OENPService

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def run_bot():
    # bot = OENPBot(
    #     bot_token=Config.TELEGRAM_BOT_TOKEN, channel_id=Config.TELEGRAM_CHANNEL_ID
    # )

    # latex_expr = r"U_{1}(x, y) = x + y \\ \delta{(a, b)} = \begin{cases}1&\text{if a = b},\\ 0  \end{cases} \\ T_{1}(n, m, k) = \delta{\left(k,m + n \right)} {\binom{m + n}{m}}"

    # image_bytes = convert_latex_to_image(latex_expr)
    # bot.post_image_to_channel(image_bytes=image_bytes, caption="Test message")
    oenp_service = OENPService("http://172.28.56.25:8000/api/v1")
    print(oenp_service.get_pyramid_by_sequence_number(1))


run_bot()
