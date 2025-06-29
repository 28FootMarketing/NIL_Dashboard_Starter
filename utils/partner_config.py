import os
import json
from pathlib import Path
import streamlit as st

CONFIG_PATH = Path(__file__).parent / "partner_configs.json"

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
        """Create config file if missing or corrupted."""
        if not CONFIG_PATH.exists():
            CONFIG_PATH.write_text(json.dumps(DEFAULT_CONFIGS, indent=2))
        else:
            try:
                with CONFIG_PATH.open("r") as f:
                    json.load(f)
            except json.JSONDecodeError:
                CONFIG_PATH.write_text(json.dumps(DEFAULT_CONFIGS, indent=2))

    @staticmethod
    def load_configs():
        """Load all partner configs from disk safely."""
        PartnerConfigHelper.initialize_defaults()
        with CONFIG_PATH.open("r") as f:
            return json.load(f)

    @staticmethod
    def get_config(partner_id="default_partner"):
        """Retrieve specific or default partner config."""
        configs = PartnerConfigHelper.load_configs()
        return configs.get(partner_id, DEFAULT_CONFIGS["default_partner"])

    @staticmethod
    def save_config(partner_id, config_data):
        """Save updated config to disk."""
        configs = PartnerConfigHelper.load_configs()
        configs[partner_id] = config_data
        with CONFIG_PATH.open("w") as f:
            json.dump(configs, f, indent=2)

    @staticmethod
    def delete_config(partner_id):
        """Remove a partner config (optional admin tool)."""
        configs = PartnerConfigHelper.load_configs()
        if partner_id in configs:
            del configs[partner_id]
            with CONFIG_PATH.open("w") as f:
                json.dump(configs, f, indent=2)

    @staticmethod
    def render_toggle_panel(partner_id="default_partner"):
        """Show visual preview of partner settings (for admins only)."""
        config = PartnerConfigHelper.get_config(partner_id)
        with st.expander(f"⚙️ {config['brand_name']} Settings Preview"):
            st.markdown(f"**Tagline:** {config['tagline']}")
            st.image(config["logo_url"], width=120)
            st.color_picker("Primary Color", config["primary_color"], key=f"preview_color_{partner_id}")
            st.write("Feature Access:")
            for feat, val in config["features"].items():
                st.checkbox(f"{feat.replace('_', ' ').title()}", value=val, key=f"preview_feat_{feat}_{partner_id}")
