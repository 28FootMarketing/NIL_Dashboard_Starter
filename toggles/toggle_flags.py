import os
import json  # ← You were also missing this import

TOGGLE_FILE = os.path.join("toggles", "toggles.json")

def load_toggle_flags():
    if os.path.exists(TOGGLE_FILE):
        with open(TOGGLE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_toggle_flags(flags):
    with open(TOGGLE_FILE, "w") as f:
        json.dump(flags, f, indent=2)
