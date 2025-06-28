# utils/partner_config.py

import streamlit as st

PARTNER_TOGGLES = {
    "enable_partner_ads": "Enable Partner Ads",
    "show_partner_badge": "Show Partner Badge",
    "display_custom_banner": "Display Custom Banner",
    "allow_partner_edits": "Allow Partner Edits"
}

    # Add more partner-specific settings here
}

def get_partner_config():
    return {k: st.session_state.get(k, v) for k, v in PARTNER_TOGGLES.items()}

def show_partner_toggle_panel():
    st.sidebar.subheader("🎛️ Partner Settings")
    for key, label in PARTNER_TOGGLES.items():
        if key not in st.session_state:
            st.session_state[key] = True
        st.sidebar.checkbox(label, key=f"partner_toggle_{key}", value=st.session_state[key])
