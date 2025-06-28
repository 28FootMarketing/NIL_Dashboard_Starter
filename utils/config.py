# utils/config.py

import json

try:
    with open("utils/partner_configs.json", "r") as f:
        PARTNER_CONFIGS = json.load(f)
except FileNotFoundError:
    PARTNER_CONFIGS = {
        "default": {
            "brand_name": "NextPlay NIL",
            "tagline": "Own your brand. Win your next play.",
            "primary_color": "#0057B8",
            "logo_url": "https://your-default-logo.com/logo.png",
            "features": {
                "pitch_deck": True,
                "deal_builder": True,
                "contract_pdf": True,
                "admin_tools": False
            },
            "contact_email": "support@nextplaynil.com"
        }
    }
