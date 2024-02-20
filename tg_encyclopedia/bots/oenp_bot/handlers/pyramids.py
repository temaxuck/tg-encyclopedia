# Awfully written. To be re-written
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from infrastructure.config import Config
from tg_encyclopedia.services.api_service import OENPService

router = Router()

oenp_service = OENPService(Config.OENP_API_URL)


@router.message(Command("pyramids"))
async def cmd_pyramids(message: Message, state: FSMContext):
    oenp_link = "https://oenp.tusur.ru/pyramid/list"
    tg_channel_link = "https://t.me/oenp_tusur"

    await message.answer(
        text=f"You can browse pyramids either on site: {oenp_link}\nOr on our telegram channel: {tg_channel_link}"
    )
