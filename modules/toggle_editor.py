import streamlit as st
import json
import os

TOGGLE_FILE = "toggles/toggle_flags.json"

def load_toggle_flags():
    if os.path.exists(TOGGLE_FILE):
        with open(TOGGLE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_toggle_flags(flags):
    with open(TOGGLE_FILE, "w") as f:
        json.dump(flags, f, indent=4)

def toggle_control_panel():
    st.subheader("🔧 Toggle Settings")

    flags = load_toggle_flags()
    allow_register = flags.get("allow_register", False)

    updated_allow_register = st.toggle("📝 Enable User Registration (Admin only)", value=allow_register)

    if updated_allow_register != allow_register:
        flags["allow_register"] = updated_allow_register
        save_toggle_flags(flags)
        st.success("✅ Registration toggle updated.")
