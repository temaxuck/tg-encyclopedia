# Awfully written. To be re-wrote
from urllib.parse import quote_plus
from typing import Any, Callable, Dict
from aiogram import Router, F, html
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardRemove,
    KeyboardButton,
    ReplyKeyboardMarkup,
    InputMediaPhoto,
)
from aiogram.types.input_file import BufferedInputFile
from aiogram.fsm.context import FSMContext
from infrastructure.config import Config
from infrastructure.utils import (
    get_pyramid_latex_representation,
    convert_latex_to_image,
)
from app.services.api_service import OENPService

router = Router()

oenp_service = OENPService(Config.OENP_API_URL)


@router.message(Command("pyramids"))
async def cmd_pyramids(message: Message, state: FSMContext):
    oenp_link = "https://oenp.tusur.ru/pyramid/list"
    tg_channel_link = "https://t.me/oenp_tusur"

    await message.answer(
        text=f"You can browse pyramids either on site: {oenp_link}\nOr on our telegram channel: {tg_channel_link}"
    )
