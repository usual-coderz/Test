import asyncio
from sky.app import start_bot, stop_bot

async def main():
    await start_bot()
    await idle()

if __name__ == "__main__":
    from pyrogram import idle
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")