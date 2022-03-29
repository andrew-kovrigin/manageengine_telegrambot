from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("согласие на обработку", request_contact=True)
        ]
    ]
)
