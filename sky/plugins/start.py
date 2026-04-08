from pyrogram import filters
from pyrogram.types import Message
from sky import sky
from sky.keyboards.start import start_inline

@sky.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    await message.reply_text(
        "🌐",
        reply_markup=start_inline
    )