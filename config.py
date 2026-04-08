import os


API_ID = int(os.getenv("API_ID", "22657083"))
API_HASH = os.getenv("API_HASH", "d6186691704bd901bdab275ceaab88f3")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8671504799:AAGStv7TDWCeNp5iaOKnY_XbGSw1AzU508Q")


OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))


MONGO_URI = os.getenv("MONGO_URI", "")


LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))


DEBUG = bool(os.getenv("DEBUG", "True") == "True")