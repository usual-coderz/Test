from pyrogram import filters
from pyrogram.types import Message
from sky.bot import bot

@bot.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply_text(
        f"Hello {message.from_user.first_name} 👋\n\nSky Bot is running!"
    )