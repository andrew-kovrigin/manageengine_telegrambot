from datetime import datetime, timedelta
from itertools import groupby

import requests
from aiogram import types

from data import config
from keyboards.inline import kb_menu, stat_menu
from loader import dp, bot
from states import FSMAdmin
from utils.helpers import change_status_name


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def main_menu(call: types.CallbackQuery):
    if call.data == "btn0":
        await bot.send_message(call.from_user.id,
                               text='[+70000000000](tel:+70000000000)',
                               parse_mode=types.ParseMode.MARKDOWN)
    if call.data == "btn1":
        bids = requests.get(config.url, params=config.json_data, headers=config.headers).json()
        tech = []
        request = bids['requests']
        request.sort(key=lambda command: command['site']['name'])
        groups = groupby(request, lambda c: c['site']['name'])
        for a, b in groups:
            tech.append(a+"\n")
            i = 0
            for c in b:
                if c['status']['name'] == 'Открыто' or c['status']['name'] == 'Утверждается':
                    date_bid = datetime.strptime(c['created_time']['display_value'], config.dateformater).date()
                    if date_bid + timedelta(days=10) >= datetime.today().date():
                        str_date = '<b>'+str(date_bid)+'</b>'
                        tech.append(f"№: {c['id']}, Дата: {str_date} !!!,"
                                    f" статус: {change_status_name(c['status']['name'])}\n")
                        i += 1
                    else:
                        tech.append(f"№: {c['id']}, Дата: {datetime.strptime(c['created_time']['display_value'], config.dateformater).date()}, статус: {change_status_name(c['status']['name'])}\n")
                        i += 1

            tech.append(f"Итого по объекту : {i}\n")
        await bot.answer_callback_query(call.id, text="")
        await bot.send_message(chat_id=call.from_user.id, text=' '.join(map(str, tech)),
                               parse_mode=types.ParseMode.HTML,
                               reply_markup=kb_menu)
    if call.data == "btn2":
        await bot.answer_callback_query(call.id, text="")
        await bot.send_message(chat_id=call.from_user.id, text="Введите номер заявки?")
        await FSMAdmin.f_query.set()
    if call.data == "btn3":
        FSMAdmin.s_query.set()
        await bot.answer_callback_query(call.id, text="")
        await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                    text='Выбрать период',
                                    reply_markup=stat_menu)
