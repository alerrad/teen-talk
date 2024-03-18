from functools import wraps

from aiogram.types import Message

from ..core import logger, redis_client
from ..lexicon import LEXICON_RU


def rate_limited(max_requests: int = 10):
    def decorator(func):
        @wraps(func)
        async def wrapper(message: Message, *args, **kwargs):
            user_id: int = message.from_user.id

            request_count = await redis_client.incr(user_id)

            if request_count > max_requests:
                username = message.from_user.username
                logger.warning(f'User {username} exceeded limit')
                await message.reply(LEXICON_RU['limit_exceeded'])

                await redis_client.expire(user_id, 3600)
                return

            return await func(message, *args, **kwargs)

        return wrapper

    return decorator
