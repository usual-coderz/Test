import asyncio
from pyrogram import idle
from sky.app import start_bot

async def main():
    await start_bot()
    print("🤖 Bot is now listening...")
    await idle()   # ⚡ THIS IS IMPORTANT

if __name__ == "__main__":
    asyncio.run(main())