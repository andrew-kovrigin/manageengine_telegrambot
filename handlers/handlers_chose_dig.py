from aiogram import types

from loader import dp
from states import FSMAdmin


@dp.message_handler(lambda message: not message.text.isdigit(), state=FSMAdmin.f_query)
async def f_query_chose_digit(message: types.Message):
    return await message.reply("Запрос должен быть в цифрах")
