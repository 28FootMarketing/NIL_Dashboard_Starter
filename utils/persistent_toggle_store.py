import json
import os

TOGGLE_FILE = "admin_toggles.json"

# Default state fallback
DEFAULT_TOGGLES = {
    "step_1": True,
    "step_2": True,
    "step_3": True,
    "step_4": True,
    "step_5": True,
    "step_6": True,
    "step_7": True,
    "show_pitch_deck": True,
    "toggle_contract": True,
    "toggle_contact_form": True,
    "enable_ads": True,
}

def load_toggles():
    """Load toggle settings from file, fallback to defaults."""
    if os.path.exists(TOGGLE_FILE):
        try:
            with open(TOGGLE_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return DEFAULT_TOGGLES.copy()
    else:
        return DEFAULT_TOGGLES.copy()

def save_toggles(toggles):
    """Save current toggle settings to file."""
    try:
        with open(TOGGLE_FILE, "w") as f:
            json.dump(toggles, f, indent=2)
    except Exception as e:
        print(f"Error saving toggles: {e}")
