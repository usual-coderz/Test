import os
import importlib

def load_plugins():
    path = "sky/plugins"
    loaded = 0

    print("\n🔌 Loading Plugins...\n")

    for file in os.listdir(path):
        if file.endswith(".py") and not file.startswith("_"):
            module = f"sky.plugins.{file[:-3]}"
            try:
                importlib.import_module(module)
                print(f"✅ {file} loaded")
                loaded += 1
            except Exception as e:
                print(f"❌ {file} error: {e}")

    print(f"\n🚀 Total Plugins Loaded: {loaded}\n")