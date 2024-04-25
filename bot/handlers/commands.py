from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from ..core import feedback_collection, logger
from ..keyboards import topics_keyboard
from ..lexicon import LEXICON_RU
from ..utils import rate_limited


commands_router = Router()


class Feedback(StatesGroup):
    feedback_text = State()


@commands_router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON_RU['start'], reply_markup=topics_keyboard)


@commands_router.message(StateFilter('*'), Command(commands='feedback'))
@rate_limited()
async def leave_feedback(message: Message, state: FSMContext):
    await state.set_state(Feedback.feedback_text)
    await message.reply(text=LEXICON_RU['feedback_entry'])


@commands_router.message(Command('cancel'))
async def cancel_command(message: Message, state: FSMContext):
    if await state.get_state() is None:
        await message.reply(LEXICON_RU['nothing_to_cancel'])
    else:
        await state.clear()
        await message.reply(LEXICON_RU['cancel'])


@commands_router.message(Feedback.feedback_text)
async def finish_feedback(message: Message, state: FSMContext):
    try:
        res = await feedback_collection.find_one_and_update(
            {
                'tg_id': message.from_user.id
            },
            {
                '$set': {
                    'feedback': message.text
                }
            }
        )
        if not res:
            await feedback_collection.insert_one({
                'tg_id': message.from_user.id,
                'feedback': message.text
            })

    except Exception:
        await message.reply(LEXICON_RU['feedback_error'])
        logger.error("Could not insert/update feedback")

    await message.reply(LEXICON_RU['finish_feedback'])
    await state.clear()
