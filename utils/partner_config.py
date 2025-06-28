# utils/partner_config.py

import streamlit as st

# ✅ Define default partner config (can be pulled from API or Sheet later)
def get_partner_config():
    return {
        "enable_partner_ads": st.session_state.get("partner_toggle_enable_partner_ads", False),
        "school_name": st.session_state.get("partner_school_name", "Default University"),
    }

# ✅ UI Panel to toggle partner-specific features
def show_partner_toggle_panel():
    st.sidebar.subheader("🎛 Partner Settings")

    # These keys must be initialized before rendering to avoid KeyError
    partner_keys = [
        "partner_toggle_enable_partner_ads",
        "partner_toggle_show_case_study",
        "partner_toggle_custom_cta",
        "partner_school_name"
    ]

    for key in partner_keys:
        if key not in st.session_state:
            st.session_state[key] = False if "enable" in key else ""

    # Partner Toggles
    st.sidebar.checkbox("Enable Partner Ads", key="partner_toggle_enable_partner_ads")
    st.sidebar.checkbox("Show Case Study Block", key="partner_toggle_show_case_study")
    st.sidebar.checkbox("Enable Custom CTA", key="partner_toggle_custom_cta")

    # Text Field
    st.sidebar.text_input("School Name", key="partner_school_name")
