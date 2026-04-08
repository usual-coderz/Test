from pyrogram import Client
import config

SKY = Client(
    "skybot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)