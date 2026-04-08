import os
import importlib
from sky import sky


def load_plugins():
    for root, _, files in os.walk("Nexa"):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                module = os.path.join(root, file).replace("/", ".")[:-3]
                importlib.import_module(module)


def start():
    load_plugins()
    print("✅ Bot Started")
    sky.run()