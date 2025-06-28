# utils/partner_config.py

import streamlit as st

PARTNER_TOGGLES = {
    "show_partner_logo": True,
    "enable_partner_ads": True,
    "display_affiliate_links": False,
}

def get_partner_config():
    """Returns current partner config states."""
    return {
        "show_partner_logo": st.session_state.get("show_partner_logo", True),
        "enable_partner_ads": st.session_state.get("enable_partner_ads", True),
        "display_affiliate_links": st.session_state.get("display_affiliate_links", False),
    }

def show_partner_toggle_panel():
    st.sidebar.subheader("🤝 Partner Display Settings")
    for key, default in PARTNER_TOGGLES.items():
        st.session_state[key] = st.sidebar.checkbox(key.replace("_", " ").title(), value=st.session_state.get(key, default))
