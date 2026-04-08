from pyrogram import filters
from pyrogram.types import Message
from sky import sky

@sky.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    await message.reply_text(
        f"Hello {message.from_user.first_name} 👋\n\nSky Bot is running! 🚀"
    )