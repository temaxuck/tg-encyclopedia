import pytest

from aiogram import types, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey
from aiogram.fsm.storage.memory import MemoryStorage

from infrastructure.config import Config
from tg_encyclopedia.bots.oenp_bot.oenp_bot import OENPBot

cfg = Config()

pytestmark = pytest.mark.asyncio


@pytest.fixture
def chat_mock():
    return types.Chat(id=123456789, type="public")


@pytest.fixture
def user_mock():
    return types.User(id=123456789, is_bot=False, first_name="test-user")


@pytest.fixture(scope="session")
def oenp_bot():
    return OENPBot(cfg.TELEGRAM_BOT_TOKEN, cfg.OENP_API_URL, cfg.OEIS_API_URL)


@pytest.fixture(scope="session")
def dp():
    return Dispatcher(storage=MemoryStorage())


@pytest.fixture
def state(oenp_bot, dp, chat_mock, user_mock):
    state = FSMContext(
        storage=dp.storage,
        key=StorageKey(
            bot_id=oenp_bot.bot.id, chat_id=chat_mock.id, user_id=user_mock.id
        ),
    )
    return state
