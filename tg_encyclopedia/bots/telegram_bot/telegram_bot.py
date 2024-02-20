import abc


class TelegramBot(abc.ABC):
    """
    Abstract class TelegramBot.

    Telegram bots are capable for posting to telegram channels
    and interacting with users
    """

    bot = None

    @abc.abstractmethod
    def __init__(self, bot_token: str) -> None:
        """
        Initialize bot.

        Must have bot (telegram.Bot) attribute

        Args:
            bot_token (str): API token recieved from @BotFather
        """
        raise NotImplemented
