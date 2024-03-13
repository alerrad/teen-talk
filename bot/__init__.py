from .core import bot, dp, logger, Config
from .handlers import commands_router, promt_router


async def start_bot():
    try:
        dp.include_routers(commands_router, promt_router)
        await bot.set_my_commands(commands=Config.BOT_COMMANDS)
        logger.info("Bot started")
        await dp.start_polling(bot)
    except Exception as _:
        await dp.stop_polling()
        logger.error("Bot stopped")