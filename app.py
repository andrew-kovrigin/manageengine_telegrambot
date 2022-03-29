from loader import dp
from utils.set_default_commands import set_default_commands
from utils.notify_admins import on_startup_notify
from aiogram import executor
import handlers


async def on_startup(dp):
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
