# utils/partner_config.py

import streamlit as st

def get_partner_config():
    return {
        "enable_partner_ads": st.session_state.get("partner_toggle_enable_partner_ads", False),
        "show_case_study": st.session_state.get("partner_toggle_show_case_study", False),
        "custom_cta": st.session_state.get("partner_toggle_custom_cta", False),
        "school_name": st.session_state.get("partner_school_name", "Default University"),
    }

def show_partner_toggle_panel():
    st.sidebar.subheader("🎛 Partner Settings")

    # ✅ Define all partner toggle defaults
    partner_defaults = {
        "partner_toggle_enable_partner_ads": False,
        "partner_toggle_show_case_study": False,
        "partner_toggle_custom_cta": False,
        "partner_school_name": "Default University"
    }

    # ✅ Ensure safe initialization for each toggle
    for key, default in partner_defaults.items():
        if key not in st.session_state or type(st.session_state[key]) != type(default):
            st.session_state[key] = default

    # ✅ Render partner config controls in sidebar
    st.sidebar.checkbox("Enable Partner Ads", key="partner_toggle_enable_partner_ads")
    st.sidebar.checkbox("Show Case Study Block", key="partner_toggle_show_case_study")
    st.sidebar.checkbox("Enable Custom CTA", key="partner_toggle_custom_cta")
    st.sidebar.text_input("School Name", key="partner_school_name")
