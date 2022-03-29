from aiogram import types

from keyboards.inline import kb_menu
from loader import dp
from utils.db import database


@dp.message_handler(content_types=['contact'])
async def request_contact(message: types.Message):
    f1 = database.search_mob(str(message.contact.phone_number))
    if f1 is False:
        await message.reply("К сожалению вы в системе не зарегистрированы")
    else:
        database.user_add_in_database(message)
        f = database.search_mob(message.contact.phone_number)
        await message.reply(f"Отлично: {list(f[0])[0]} {list(f[0])[1]} в системе данные о вас найдены!", remove_keyboard=True, reply_markup=kb_menu)
