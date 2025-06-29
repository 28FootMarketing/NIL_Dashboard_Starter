# utils/partner_config.py

import os
import json
import streamlit as st

CONFIG_PATH = "utils/partner_configs.json"

DEFAULT_CONFIGS = {
    "default_partner": {
        "brand_name": "NextPlay NIL",
        "tagline": "Own your brand. Win your next play.",
        "primary_color": "#0a6cf1",
        "logo_url": "https://nextplay.ai/logo.png",
        "contact_email": "info@nextplay.ai",
        "enable_partner_ads": True,
        "features": {
            "pitch_deck": True,
            "deal_builder": True,
            "contract_pdf": True,
            "admin_tools": True
        }
    }
}


class PartnerConfigHelper:

    @staticmethod
    def initialize_defaults():
        """Create config file if it does not exist."""
        if not os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "w") as f:
                json.dump(DEFAULT_CONFIGS, f, indent=2)

    @staticmethod
    def load_configs():
        """Load all partner configs."""
        if not os.path.exists(CONFIG_PATH):
            PartnerConfigHelper.initialize_defaults()
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)

    @staticmethod
    def get_config(partner_id="default_partner"):
        """Retrieve config for current or default partner."""
        configs = PartnerConfigHelper.load_configs()
        return configs.get(partner_id, DEFAULT_CONFIGS["default_partner"])

    @staticmethod
    def save_config(partner_id, config_data):
        """Save updated config for a given partner."""
        configs = PartnerConfigHelper.load_configs()
        configs[partner_id] = config_data
        with open(CONFIG_PATH, "w") as f:
            json.dump(configs, f, indent=2)

    @staticmethod
    def render_toggle_panel():
        """Optional: Show partner toggles visually (for admins)."""
        config = PartnerConfigHelper.get_config()
        with st.expander("⚙️ Partner Toggles"):
            st.markdown(f"**Brand:** {config['brand_name']}")
            st.markdown(f"**Tagline:** {config['tagline']}")
            st.color_picker("Primary Color", config["primary_color"], key="panel_primary_color")
            st.write("Feature Access:")
            for feature, value in config["features"].items():
                st.checkbox(f"{feature.replace('_', ' ').title()}", value=value, key=f"panel_{feature}")
