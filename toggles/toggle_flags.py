import streamlit as st
import json
import os
from utils.audit_logger import log_event  # ✅ Log toggle changes

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
    st.subheader("🔧 Feature Toggle Settings")

    flags = load_toggle_flags()

    st.markdown("Enable or disable features available to different user roles.")
    
    toggle_config = {
        "allow_register": "📝 Enable User Registration",
        "enable_feedback": "🗒️ Enable Tester Feedback Form",
        "maintenance_mode": "🚧 Maintenance Mode (Disable all dashboards)",
        "show_beta_features": "🧪 Show Beta Features to Admins"
    }

    for key, label in toggle_config.items():
        current_value = flags.get(key, False)
        new_value = st.toggle(label, value=current_value)

        if new_value != current_value:
            flags[key] = new_value
            save_toggle_flags(flags)
            log_event("toggle_change", st.session_state.get("user_email", "unknown"), f"{key} changed to {new_value}")
            st.success(f"✅ '{label}' updated.")

    st.markdown("---")
    st.caption("Changes are saved instantly and affect live dashboard behavior.")
