import os
import pwd

from argparse import ArgumentTypeError
from configargparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from typing import Callable
from yarl import URL

from .config import Config


def validate(type: Callable, constraint: Callable) -> Callable:

    def wrapper(value):
        try:
            value = type(value)
            if not constraint(value):
                raise ArgumentTypeError(f"Value {value} doesn't meet constraints")
        except ValueError:
            raise ArgumentTypeError(f"Couldn't typecast value {value} to type {type}")

        return value

    return wrapper


"""
Type validation handlers:
"""
positive_int = validate(int, lambda x: x > 0)


def get_arg_parser(cfg: Config = None) -> ArgumentParser:

    if cfg is None:
        cfg = Config()

    parser = ArgumentParser(
        auto_env_var_prefix=cfg.ENV_VAR_PREFIX,
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    group = parser.add_argument_group("Bots' common settings")
    group.add_argument(
        "--bot-token",
        default=cfg.TELEGRAM_BOT_TOKEN,
        help="Telegram API token recieved from @BotFather",
    )
    group.add_argument(
        "--oenp-api-url",
        type=URL,
        default=cfg.OENP_API_URL,
        help="URL of Online Encyclopedia of Number Pyramids API",
    )

    group = parser.add_argument_group("OENP channel bot's settings")
    group.add_argument(
        "--channel-id",
        default=cfg.TELEGRAM_CHANNEL_ID,
        help="Id of telegram channel to post pyramids to",
    )
    group.add_argument(
        "-s",
        "--start",
        type=positive_int,
        required=True,
        help="Start of range of Pyramid's sequence numbers to post to channel",
    )
    group.add_argument(
        "-e",
        "--end",
        type=positive_int,
        required=True,
        help="End of range of Pyramid's sequence numbers to post to channel",
    )
    group.add_argument(
        "-l",
        "--latency",
        type=positive_int,
        default=60,
        help="Latency between posts to channel (Telegram does not allow to spam channel)",
    )

    group = parser.add_argument_group("Logging options")
    group.add_argument(
        "--log-level",
        default=cfg.LOG_LEVEL,
        choices=("debug", "info", "warning", "error", "fatal"),
    )

    # clear env variables after parser parsed all the necessary args
    clear_env(lambda env_var: env_var.startswith(cfg.ENV_VAR_PREFIX))

    return parser


def clear_env(rule: Callable) -> None:
    """
    Clear vulnerable environment variables such as database url connection
    """

    for name in filter(rule, tuple(os.environ)):
        os.environ.pop(name)
