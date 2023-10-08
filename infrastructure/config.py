from dotenv import load_dotenv
import os

load_dotenv()  # load dotenv file


class Config:
    """Config
    Stores config variables needed to run project

    Raises:
        ValueError: Config couldn't find necessary environment variables
    """

    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

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
