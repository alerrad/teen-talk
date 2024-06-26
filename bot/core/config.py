from aiogram.types import BotCommand
from dotenv import get_key


class Config:
    BOT_TOKEN: str = get_key(".env", "BOT_TOKEN")
    HUGGINGFACE_KEY: str = get_key(".env", "HUGGINGFACE_KEY")
    MODEL_API_URL: str = get_key(".env", "MODEL_API_URL")
    MONGO_URI: str = get_key(".env", "MONGO_URI")

    BOT_COMMANDS = [
        BotCommand(command="start", description="Старт"),
        BotCommand(command="feedback", description="Написать отзыв"),
        BotCommand(command="cancel", description="Отменить текущую операцию")
    ]

    TOPICS = ["моё тело", "психология", "репродукция", "половое влечение"]
