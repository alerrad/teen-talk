from .core import bot, dp, logger, Config


async def start_bot():
    try:
        await bot.set_my_commands(commands=Config.BOT_COMMANDS)
        logger.info("Bot started")
        await dp.start_polling(bot)
    except Exception as _:
        await dp.stop_polling()
        logger.error("Bot stopped")