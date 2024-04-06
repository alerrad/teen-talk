from aiogram.types import BotCommand
from dotenv import get_key


class Config:
    BOT_TOKEN: str = get_key(".env", "BOT_TOKEN")
    HUGGINGFACE_KEY: str = get_key(".env", "HUGGINGFACE_KEY")
    MODEL_API_URL: str = get_key(".env", "MODEL_API_URL")
    MONGO_URI: str = get_key(".env", "MONGO_URI")

    BOT_COMMANDS = [
        BotCommand(command="start", description="start the bot"),
        BotCommand(command="feedback", description="leave a feedback about the bot"),
        BotCommand(command="cancel", description="cancel current operation")
    ]
