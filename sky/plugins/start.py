from pyrogram import filters
from pyrogram.types import Message
from sky import sky
from sky.keyboards.start import start_button

@sky.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    await client.send_message(
        chat_id=message.chat.id,
        text="🌐",
        reply_markup=start_button()
    )