from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    """Config
    Stores config variables needed to run project

    Raises:
        ValueError: Config couldn't find necessary environment variables
    """

    ENV_VAR_PREFIX = "TG_ENCYCLOPEDIA_"
    TELEGRAM_BOT_TOKEN = os.getenv(f"{ENV_VAR_PREFIX}BOT_TOKEN")
    TELEGRAM_CHANNEL_ID = os.getenv(f"{ENV_VAR_PREFIX}CHANNEL_ID")
    OENP_API_URL = os.getenv(f"{ENV_VAR_PREFIX}OENP_API_URL")
    OEIS_API_URL = "https://oeis.org/"
    TELEGRAM_POST_FORMAT = {
        "font_size": 20,
        "padding": 40,
    }
    LOG_LEVEL = "INFO"

    @classmethod
    def validate_config(cls):
        if not cls.TELEGRAM_BOT_TOKEN:
            raise ValueError(
                "TELEGRAM_BOT_TOKEN is not set in the environment variables."
            )

        if not cls.TELEGRAM_CHANNEL_ID:
            raise ValueError(
                "TELEGRAM_CHANNEL_ID is not set in the environment variables."
            )

        if not cls.OENP_API_URL:
            raise ValueError("OENP_API_URL is not set in the environment variables.")
