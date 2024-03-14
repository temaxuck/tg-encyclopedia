from datetime import datetime
from unittest.mock import AsyncMock


def create_message(chat, user, text, bot=None):
    return AsyncMock(
        message_id=1,
        chat=chat,
        from_user=user,
        text=text,
        date=datetime.now(),
        bot=bot,
    )


def get_api_response_mock(_):
    return {
        "id": 1,
        "sequence_number": 1,
        "generating_function": [
            {"name": "U", "variables": "x, y", "expression": "x + y", "is_main": True}
        ],
        "explicit_formula": [
            {
                "name": "T",
                "variables": "n, m, k",
                "expression": "delta(k, m + n)*binomial(m + n, m)",
                "limitation": "",
            }
        ],
        "data": [
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        "statuscode": 0,
        "gf_latex": "U_{1}(x, y) = x + y ",
        "ef_latex": "\\delta{(a, b)} = \\begin{cases}1&\\text{if a = b},\\\\ 0  \\end{cases}  \\\\ T_{1}(n, m, k) = \\delta{\\left(k,m + n \\right)} {\\binom{m + n}{m}}",
        "author": {"username": "temax", "profile_image": "1//c2071b799d96e370.png"},
    }
