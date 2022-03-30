from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import kb_start
from keyboards.inline import kb_menu
from loader import dp

from utils.db import database


@dp.message_handler(Command("start"))
async def command_start(message: types.Message):
    known_user = database.search_user_id(message.from_user.id)
    print(known_user)
    if known_user is False:
        await message.answer("Добрый день, вы подключились к автоматизированной системе компании <b>OOO "
                             "'---'</b>\n"
                             " Для того, чтобы оставить заявку или задать вопрос, необходимо"
                             " Ваше согласие на обработку персональных данных."
                             " Это нужно для того чтобы система смогла авторизовать Вас!", reply_markup=kb_start,
                             parse_mode=types.ParseMode.HTML)
    else:
        f2 = database.search_user_on_id(message.from_user.id)
        await message.answer(f"Добрый день, {f2[0][0]} {f2[0][1]}, что у вас случилось?", reply_markup=kb_menu)
