from aiogram import types

from keyboards.inline import kb_menu
from loader import dp, bot


@dp.callback_query_handler(lambda command: command.data and command.data.startswith('back'))
async def button_back(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                text='Что у вас случалось?',
                                parse_mode=types.ParseMode.MARKDOWN,
                                reply_markup=kb_menu)
