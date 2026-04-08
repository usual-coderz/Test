from pyrogram import Client
import config

sky = Client(
    "skybot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)