# utils/partner_config.py

import streamlit as st

PARTNER_TOGGLES = {
    "enable_partner_ads": True,
    # Add more partner-specific settings here
}

def get_partner_config():
    return {k: st.session_state.get(k, v) for k, v in PARTNER_TOGGLES.items()}

def show_partner_toggle_panel():
    st.sidebar.subheader("🔧 Partner Settings")
    for key in PARTNER_TOGGLES:
        if key not in st.session_state:
            st.session_state[key] = PARTNER_TOGGLES[key]
        st.sidebar.checkbox(key.replace("_", " ").title(), key=key, value=st.session_state[key])
