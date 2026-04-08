from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    await message.reply_text(
        f"Hello {message.from_user.first_name} 👋\n\nSky Bot is running!"
    )