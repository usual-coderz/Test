from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from sky.utils.loader import load_plugins

bot = Client(
    "sky-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


load_plugins()