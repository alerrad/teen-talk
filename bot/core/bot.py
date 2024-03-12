from aiogram import Bot, Dispatcher

from . import Config


bot = Bot(Config.BOT_TOKEN)
dp = Dispatcher()
