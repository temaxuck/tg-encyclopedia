import logging
import os

from telegram.error import TelegramError


def set_logging(log_level=logging.INFO, filename="logs/tg.log"):
    """set logging

    Args:
        filename: file to output logs, by default logs/tg.log (logging in terminal)
    """

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=log_level,
        filename=filename,
        filemode="w",
    )


def log_telegram_error(f):
    """
    Decorator for async functions which logs occuring telegram.error Exception

    Args:
        f: async function which make telegram actions
    """

    async def wrapper(*args, **kwargs):
        try:
            return await f(*args, **kwargs)
        except TelegramError as e:
            message = (
                f"Telegram error occured in function: {f.__name__} "
                f"when calling it with arguments: {args} {kwargs}. "
                f"Exception: {e}."
            )
            print(message)
            logging.error(message)

            raise e
        except Exception as e:
            message = (
                f"Unknown error occured in function: {f.__name__} "
                f"when calling it with arguments: {args} {kwargs}. "
                f"Exception: {e}."
            )
            print(message)
            logging.error(message)

    return wrapper
