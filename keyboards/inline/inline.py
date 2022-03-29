from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_menu = InlineKeyboardMarkup(row_width=3,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton('Активные заявки', callback_data='btn1'),
                                       InlineKeyboardButton('Статистика', callback_data='btn3'),
                                       InlineKeyboardButton('Подробно по №', callback_data='btn2')

                                   ],
                                   [
                                       InlineKeyboardButton('Связь с диспетчером', callback_data='btn0')
                                   ]
                               ])


stat_menu = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton('Прошлый месяц', callback_data='stat2'),
                                         InlineKeyboardButton('Текущий месяц', callback_data='stat1'),
                                     ],
                                     [
                                         InlineKeyboardButton('Назад', callback_data='back')
                                     ]
                                 ])
