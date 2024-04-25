from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


topics_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="моё тело"), KeyboardButton(text="психология")],
        [KeyboardButton(text="репродукция"), KeyboardButton(text="половое влечение")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
