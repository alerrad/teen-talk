from aiogram.types import BotCommand
from dotenv import get_key


class Config:
    BOT_TOKEN: str = get_key(".env", "BOT_TOKEN")

    BOT_COMMANDS = [
        BotCommand(command="start", description="start the bot"),
        BotCommand(command="feedback", description="leave a feedback about the bot"),
        BotCommand(command="cancel", description="cancel current operation")
    ]

    MONGO_URI: str = get_key(".env", "MONGO_URI")
