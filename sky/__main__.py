from pyrogram import Client
import config
import os
import importlib

sky = Client(
    "skybot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

def load_plugins():
    for root, _, files in os.walk("sky/plugins"):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                module = os.path.join(root, file).replace("/", ".")[:-3]
                importlib.import_module(module)
                print(f"✅ Loaded: {module}")

if __name__ == "__main__":
    print("🔌 Loading Plugins...\n")
    load_plugins()
    print("\n🚀 Bot Started!\n")
    sky.run()