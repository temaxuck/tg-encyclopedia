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


class SearchType:
    name: str
    query_example: str
    query_callback: Callable

    def __init__(self, name: str, query_example: str, query_callback: Callable):
        self.name = name
        self.query_example = query_example
        self.query_callback = query_callback


def get_search_type_by_name(
    search_type_list: list[SearchType], name: str
) -> SearchType:
    for search_type in search_type_list:
        if name == search_type.name:
            return search_type

    return None


def get_pyramid_json_from_api_response(api_response: Dict[str, Any]) -> Dict[str, Any]:
    if exact := api_response.get("exact"):
        return exact[0]
    elif related := api_response.get("related"):
        return related[0]
    elif api_response.get("id"):
        return api_response
    else:
        return None


class Search(StatesGroup):
    search_types = [
        SearchType(
            "By sequence number", "12", oenp_service.get_pyramid_by_sequence_number
        ),
        SearchType(
            "By generating function",
            "(1 + y) / (1 - x - x * y)",
            oenp_service.search_pyramid_by_generating_function,
        ),
        SearchType(
            "By explicit formula",
            "k * binomial(k + n, m) * binomial(k + n, n) / (k + n)",
            oenp_service.search_pyramid_by_explicit_formula,
        ),
        SearchType(
            "By data table",
            "1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 3, 3, 1, 0, 0, 0, 1, 4, 6, 4, 1, 0, 0, 1, 5, 10, 10, 5, 1, 0, 1, 6, 15, 20, 15, 6, 1, 1, 7, 21, 35, 35, 21, 7",
            oenp_service.search_pyramid_by_data,
        ),
    ]
    choosing_search_type = State()
    search_input = State()


@router.message(Command("find_pyramid"))
async def cmd_find_pyramid(message: Message, state: FSMContext):
    keyboard = [
        [KeyboardButton(text=search_type.name)] for search_type in Search.search_types
    ]
    await message.answer(
        text="Choose type of search:",
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True),
    )

    await state.set_state(Search.choosing_search_type)


@router.message(
    Search.choosing_search_type,
    F.text.in_([search_type.name for search_type in Search.search_types]),
)
async def search_type_chosen(message: Message, state: FSMContext):
    search_type = get_search_type_by_name(Search.search_types, message.text)

    if not search_type:
        keyboard = [
            [KeyboardButton(text=search_type.name)]
            for search_type in Search.search_types
        ]
        await message.answer(
            text="Choose type of search:",
            reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True),
        )

        await state.set_state(Search.choosing_search_type)
        return

    await state.update_data(search_type=search_type)
    await message.answer(
        text=f"Enter search query\nExample: {html.code(search_type.query_example)}",
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="HTML",
    )
    await state.set_state(Search.search_input)


@router.message(Search.choosing_search_type)
async def search_type_chosen(message: Message, state: FSMContext):
    keyboard = [
        [KeyboardButton(text=search_type.name)] for search_type in Search.search_types
    ]
    await message.answer(
        text="There's no such type of search. Please, choose type of search:",
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True),
    )


@router.message(Search.search_input)
async def search(message: Message, state: FSMContext):
    await state.update_data(search_input=message.text)
    state_data = await state.get_data()
    search_type = state_data.get("search_type")
    api_response = search_type.query_callback(message.text)
    pyramid_json = get_pyramid_json_from_api_response(api_response)

    if pyramid_json == None:
        await message.answer(text="Nothing has been found")
        return

    pyramid_latex = get_pyramid_latex_representation(
        pyramid_json.get("sequence_number"),
        pyramid_json.get("gf_latex"),
        pyramid_json.get("ef_latex"),
    )
    oenp_link = f"https://oenp.tusur.ru/search?search_type={1 if search_type.name == 'By data table' else 0}&q={quote_plus(message.text)}"
    pyramid_image = convert_latex_to_image(pyramid_latex)

    await message.answer_photo(
        photo=BufferedInputFile(pyramid_image.read(), filename="pyramid_latex.png"),
        caption="\n".join(
            (
                f"<b>Data table:</b>",
                f"<code>{pyramid_json.get('data')}</code>",
                f"This is the search result for your query: <i>{html.quote(message.text)}</i>.\nFor more results follow this link: {oenp_link}",
            )
        ),
        parse_mode="HTML",
    )
