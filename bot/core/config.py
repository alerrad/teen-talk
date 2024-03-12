from os import environ as env

from aiogram.types import BotCommand
from dotenv import load_dotenv


load_dotenv()


class Config:
    BOT_TOKEN: str = env.get("BOT_TOKEN")

    BOT_COMMANDS = [
        BotCommand(command="start", description="start the bot"),
        BotCommand(command="feedback", description="leave a feedback about the bot"),
    ]

    MONGO_URI: str = env.get("MONGO_URI")
