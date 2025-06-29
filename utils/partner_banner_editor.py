import streamlit as st
import json
import os

PARTNER_CONFIG_PATH = "config/partner_config.json"

def load_partner_config():
    if not os.path.exists(PARTNER_CONFIG_PATH):
        return {}
    with open(PARTNER_CONFIG_PATH, "r") as f:
        return json.load(f)

def save_partner_config(config):
    with open(PARTNER_CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

def show_partner_banner_editor():
    st.subheader("🎨 Partner Banner Editor")
    
    config = load_partner_config()

    # Get current values or set defaults
    show_banner = config.get("partner_toggle_show_banner", False)
    banner_msg = config.get("partner_banner_message", "This version is customized for your NIL partner program.")

    # Form for editing
    with st.form("banner_editor_form"):
        updated_show = st.checkbox("✅ Show Partner Banner", value=show_banner)
        updated_msg = st.text_area("✏️ Partner Banner Message (HTML allowed)", value=banner_msg, height=150)
        submitted = st.form_submit_button("💾 Save Banner Settings")

        if submitted:
            config["partner_toggle_show_banner"] = updated_show
            config["partner_banner_message"] = updated_msg
            save_partner_config(config)
            st.success("✅ Partner banner settings saved!")
