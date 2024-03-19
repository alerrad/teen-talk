from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from . import Config


bot = Bot(Config.BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
