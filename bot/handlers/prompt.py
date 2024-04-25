import aiohttp
from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from ..core import Config, question_collection
from ..lexicon import LEXICON_RU, QNA
from ..utils import rate_limited


promt_router = Router()


class Topic(StatesGroup):
    topic_name = State()


@promt_router.message(StateFilter(None))
async def handle_topic(message: Message, state: FSMContext):
    if message.text not in Config.TOPICS:
        await message.reply(LEXICON_RU['no_topic'])
        return

    await state.update_data(topic=message.text)
    await state.set_state(Topic.topic_name)
    await message.reply(LEXICON_RU['topic_chosen'])


@promt_router.message(Topic.topic_name)
@rate_limited()
async def handle_question(message: Message, state: FSMContext):
    if message.text in Config.TOPICS:
        await state.update_data(topic=message.text)
        await message.reply(LEXICON_RU['topic_chosen'])
        return

    try:
        data = await state.get_data()
        topic: str = data['topic']
        QUESTIONS = list(QNA[topic].keys())

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

            if (max_weight := max(weights)) < 0.7:
                await message.reply(LEXICON_RU['no_answer'])

                if max_weight >= 0.4:
                    await question_collection.insert_one({
                        'question': message.text,
                        'choosen_category': topic,
                        'max_semantic_similarity_score': max_weight
                    })

                return

            match_question = QUESTIONS[weights.index(max_weight)]
            await message.reply(QNA[topic][match_question])

    except Exception:
        await message.reply(text=LEXICON_RU['no_answer'])
