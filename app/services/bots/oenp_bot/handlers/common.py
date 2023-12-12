from urllib.parse import quote_plus
from typing import Any, Callable, Dict
from aiogram import Router, F, html
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardRemove,
)
from aiogram.fsm.context import FSMContext
from app.services.api_service import OENPService
from ..handlers import COMMANDS

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        text=f"Welcome to Online Encyclopedia of Number Pyramids telegram bot! Type /help to see available commands."
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        text="\n".join(
            (
                "This is Online Encyclopedia of Number Pyramids telegram bot.",
                "",
                "<b>What is Online Encyclopedia of Number Pyramids?</b>",
                "You can read about <b>Online Encyclopedia of Number Pyramids</b> on https://oenp.tusur.ru/book",
                "",
                "<b>Commands</b>",
                "\n".join(
                    [
                        f"{command} - {description}"
                        for command, description in COMMANDS.items()
                    ]
                ),
            )
        ),
        parse_mode="HTML",
    )


@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Actions cancelled", reply_markup=ReplyKeyboardRemove())
