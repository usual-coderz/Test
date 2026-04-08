import os


API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")


OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))


MONGO_URI = os.getenv("MONGO_URI", "")


LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))


DEBUG = bool(os.getenv("DEBUG", "True") == "True")