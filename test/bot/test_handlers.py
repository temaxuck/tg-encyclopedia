import pytest

from aiogram import types, html
from urllib.parse import quote_plus

from tg_encyclopedia.bots.oenp_bot.handlers.search import (
    Search as SearchStateGroup,
    cmd_find_pyramid,
    search,
    search_type_chosen,
)
from test.bot.utils import create_message, get_api_response_mock


@pytest.mark.asyncio
async def test_cmd_find_pyramid(state, chat_mock, user_mock):
    message = create_message(chat_mock, user_mock, r"/find_pyramid")
    await cmd_find_pyramid(message, state)

    keyboard = [
        [types.KeyboardButton(text=search_type.name)]
        for search_type in SearchStateGroup.search_types
    ]
    message.answer.assert_called_with(
        text="Choose type of search:",
        reply_markup=types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True),
    )
    assert await state.get_state() == SearchStateGroup.choosing_search_type


@pytest.mark.asyncio
async def test_search_type_chosen(state, chat_mock, user_mock):
    await state.set_state(SearchStateGroup.choosing_search_type)

    message = create_message(chat_mock, user_mock, "Wrong search type")
    await search_type_chosen(message, state)

    assert await state.get_state() == SearchStateGroup.choosing_search_type


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "search_type",
    SearchStateGroup.search_types,
)
async def test_search(state, chat_mock, user_mock, search_type):
    await state.update_data(search_type=search_type)
    await state.set_state(SearchStateGroup.search_input)
    search_type.query_callback = get_api_response_mock

    message = create_message(chat_mock, user_mock, search_type.query_example)
    await search(message, state)

    api_response = get_api_response_mock(...)
    oenp_link = f"https://oenp.tusur.ru/search?search_type={1 if search_type.name == 'By data table' else 0}&q={quote_plus(message.text)}"
    kwargs = message.answer_photo.call_args.kwargs

    assert kwargs.get("caption") == "\n".join(
        (
            f"<b>Data table:</b>",
            f"<code>{api_response.get('data')}</code>",
            f"This is the search result for your query: <i>{html.quote(message.text)}</i>.\nFor more results follow this link: {oenp_link}",
        )
    )

    assert await state.get_state() == SearchStateGroup.search_input
