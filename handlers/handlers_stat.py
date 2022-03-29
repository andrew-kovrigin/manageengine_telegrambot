from datetime import datetime
from itertools import groupby

import requests
from aiogram import types

from data import config
from keyboards.inline import kb_menu
from loader import dp, bot


@dp.callback_query_handler(lambda command: command.data and command.data.startswith('stat'))
async def button_stat(call: types.CallbackQuery):
    bids = requests.get(config.url, params=config.json_data, headers=config.headers).json()
    now = datetime.now()
    now_moths = now.month
    tech = []
    request = bids['requests']
    request.sort(key=lambda command: command['site']['name'])
    groups = groupby(request, lambda command: command['site']['name'])
    if call.data == 'stat1':
        i, s, c, u, o, f, v, y = 0, 0, 0, 0, 0, 0, 0, 0
        for a, b_components in groups:
            tech.append(a + "\n")
            i, s, c, u = 0, 0, 0, 0
            for c_com in b_components:
                dates = datetime.strptime(c_com['created_time']['display_value'], config.dateformater)
                if dates.month == now_moths:
                    o += 1
                    i += 1
                    if c_com['status']['name'] == 'Открыто':
                        s += 1
                        f += 1
                    elif c_com['status']['name'] == 'Закрыто':
                        c += 1
                        v += 1
                    elif c_com['status']['name'] == 'Утверждается':
                        u += 1
                        y += 1

            await bot.send_message(chat_id=call.from_user.id, text=f'{a}\n Открытых заявок: {s} '
                                                                   f'\nЗакрытых заявок: {c} '
                                                                   f'\nЗаявок на утверждении: {u} '
                                                                   f'\nВсего заявок по объекту: {i}',
                                   parse_mode=types.ParseMode.MARKDOWN)
        await bot.send_message(chat_id=call.from_user.id, text=f"Итого всего заявок: {o} "
                                                               f"\nиз них открыто {f}"
                                                               f"\nзакрыто: {v}"
                                                               f"\nна утверждении: {y}",
                               reply_markup=kb_menu)
    elif call.data == 'stat2':
        i, s, c, u, o, f, v, y = 0, 0, 0, 0, 0, 0, 0, 0
        for a, b_components in groups:
            tech.append(a + "\n")
            i, s, c, u = 0, 0, 0, 0
            for c_com in b_components:
                dates = datetime.strptime(c_com['created_time']['display_value'], config.dateformater)
                if dates.month == now_moths - 1:
                    o += 1
                    i += 1
                    if c_com['status']['name'] == 'Открыто':
                        s += 1
                        f += 1
                    elif c_com['status']['name'] == 'Закрыто':
                        c += 1
                        v += 1
                    elif c_com['status']['name'] == 'Утверждается':
                        u += 1
                        y += 1

            await bot.send_message(chat_id=call.from_user.id, text=f'{a}\n Открытых заявок: {s} '
                                                                   f'\nЗакрытых заявок: {c} '
                                                                   f'\nЗаявок на утверждении: {u} '
                                                                   f'\nВсего заявок по объекту: {i}',
                                   parse_mode=types.ParseMode.MARKDOWN)
        await bot.send_message(chat_id=call.from_user.id, text=f"Итого всего заявок: {o} "
                                                               f"\nиз них открыто {f}"
                                                               f"\nзакрыто: {v}"
                                                               f"\nна утверждении: {y}",
                               reply_markup=kb_menu)
