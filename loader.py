import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config


if not config.token:
    print("Ошибка: нет токена, бот работать небудет")
loop = asyncio.get_event_loop()
bot = Bot(token=config.token)
storage = MemoryStorage()
dp = Dispatcher(bot, loop=loop, storage=storage)
