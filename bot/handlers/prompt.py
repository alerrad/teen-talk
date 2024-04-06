import aiohttp
from aiogram import Router
from aiogram.types import Message

from ..core import Config
from ..lexicon import LEXICON_RU, QNA, QUESTIONS
from ..utils import rate_limited


promt_router = Router()


@promt_router.message()
@rate_limited()
async def handle_question(message: Message):
    try:
        headers = {
            'Authorization': f"Bearer {Config.HUGGINGFACE_KEY}"
        }
        payload = {
            'inputs': {
                'source_sentence': message.text.lower(),
                'sentences': QUESTIONS
            }
        }

        async with aiohttp.ClientSession() as session:
            res = await session.post(Config.MODEL_API_URL, json=payload, headers=headers)
            weights: list[int] = await res.json()

            if (max_weight := max(weights)) < 0.6:
                await message.reply(LEXICON_RU['no_answer'])
                return

            match_question = QUESTIONS[weights.index(max_weight)]
            await message.reply(QNA[match_question])

    except Exception:
        await message.reply(text=LEXICON_RU['no_answer'])
