from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('help'))
async def command_help(message: types.Message):
    await message.reply("На любые вопросы связанные с ботом может ответить диспетчер")