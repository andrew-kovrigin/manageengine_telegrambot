from datetime import datetime

import html2text
import requests
from aiogram import types
from aiogram.dispatcher import FSMContext

from data import config
from keyboards.inline import kb_menu
from loader import dp
from states import FSMAdmin


@dp.message_handler(lambda message: message.text.isdigit(), state=FSMAdmin.f_query)
async def f_query_ok(message: types.Message, state: FSMContext):
    url = config.url + str(message.text)
    bids = requests.get(url=url, headers=config.headers).json()
    if bids['response_status']['status'] == "success":
        bid = bids['request']
        if bid['technician'] is None:
            tech = 'Не назначен'
        else:
            tech = bid['technician']['name']
        await state.finish()
        return await message.reply(f"Заявка №: {bid['id']}"
                                   f"\nДата: {datetime.strptime(bid['created_time']['display_value'], config.dateformater).date()} "
                                   f"\nЧто случилось, Кратко: \n{html2text.html2text(bid['description'])}"
                                   f"\nСтатус: {bid['status']['name']}"
                                   f"\nКто решил: {tech}", parse_mode=types.ParseMode.HTML, reply_markup=kb_menu)
    else:
        return await message.reply("Увы, такой заявки нет,"
                                   " попробуйте еще раз! напишите "
                                   "/cancel или отмена")
