from .core import bot, dp, logger, redis_client, Config
from .handlers import commands_router, promt_router


async def start_bot() -> None:
    try:
        if await redis_client.ping():
            logger.info("Redis connected")
        else:
            logger.error("Redis not connected")
            raise ConnectionError("Failed to connect redis")
        
        dp.include_routers(commands_router, promt_router)
        await bot.set_my_commands(commands=Config.BOT_COMMANDS)
        logger.info("Bot started")
        await dp.start_polling(bot)
    
    except Exception as _:
        await dp.stop_polling()
        logger.error("Bot stopped")