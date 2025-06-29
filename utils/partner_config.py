import streamlit as st

def get_partner_config():
    return {
        "partner_tier": "Gold",
        "enable_partner_ads": st.session_state.get("partner_toggle_enable_partner_ads", False),
    }

def show_partner_toggle_panel():
    st.markdown("### ⚙️ Partner Visibility Toggles")
    st.checkbox("Show Partner Logo", key="partner_toggle_logo")
    st.checkbox("Enable Partner Ads", key="partner_toggle_enable_partner_ads")
    st.checkbox("Display Partner Metrics", key="partner_toggle_metrics")
