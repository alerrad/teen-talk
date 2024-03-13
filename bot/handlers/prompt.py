from aiogram import Router
from aiogram.types import Message

from ..lexicon import LEXICON_RU


promt_router = Router()


@promt_router.message()
async def handle_question(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_answer'])
