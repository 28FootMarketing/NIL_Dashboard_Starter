# utils/partner_config.py

import streamlit as st

PARTNER_TOGGLES = {
    "enable_partner_ads": "Enable Partner Ads",
    "show_partner_badge": "Show Partner Badge",
    "display_custom_banner": "Display Custom Banner",
    "allow_partner_edits": "Allow Partner Edits"
}

def show_partner_toggle_panel():
    st.sidebar.subheader("🎛️ Partner Settings")
    for key, label in PARTNER_TOGGLES.items():
        unique_key = f"partner_toggle_{key}"
        if unique_key not in st.session_state:
            st.session_state[unique_key] = True
        st.session_state[unique_key] = st.sidebar.checkbox(label, key=unique_key, value=st.session_state[unique_key])
