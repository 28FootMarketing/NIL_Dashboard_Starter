# ✅ partner_config.py

import streamlit as st

PARTNER_TOGGLES = {
    "partner_toggle_hide_quiz": "Hide Quiz Section",
    "partner_toggle_enable_partner_ads": "Enable Partner Ads",
    "partner_toggle_allow_contact_form": "Show Partner Contact Form",
    "partner_toggle_enable_pitch": "Enable Partner Pitch Deck Section",
}

def get_partner_config():
    return {key: st.session_state.get(key, False) for key in PARTNER_TOGGLES.keys()}

def show_partner_toggle_panel():
    st.subheader("🎛️ Partner Settings Panel")
    for key, label in PARTNER_TOGGLES.items():
        current_val = st.session_state.get(key, False)
        new_val = st.checkbox(label, value=current_val, key=f"partner_toggle_panel_{key}")
        st.session_state[key] = new_val
