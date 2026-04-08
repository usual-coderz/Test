from sky.bot import bot

async def start_bot():
    await bot.start()
    print("🚀 Bot Started!")

async def stop_bot():
    await bot.stop()
    print("🛑 Bot Stopped!")