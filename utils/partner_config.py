import streamlit as st

class PartnerConfigHelper:
    DEFAULTS = {
        "partner_toggle_enable_partner_ads": False,
        "partner_toggle_show_case_study": False,
        "partner_toggle_custom_cta": False,
        "partner_school_name": "Default University",
        "partner_cta_message": "Join our NIL community and unlock new opportunities!",
        "partner_cta_button_text": "Get Started",
        "partner_cta_url": "https://example.com",
        "show_partner_config_panel": False
    }

    @classmethod
    def initialize_defaults(cls):
        for key, default in cls.DEFAULTS.items():
            if key not in st.session_state or type(st.session_state[key]) != type(default):
                st.session_state[key] = default

    @classmethod
    def get_config(cls):
        return {
            "enable_partner_ads": st.session_state.get("partner_toggle_enable_partner_ads", False),
            "school_name": st.session_state.get("partner_school_name", "Default University"),
        }

    @classmethod
    def render_toggle_panel(cls):
        if st.session_state.get("show_partner_config_panel", False):
            st.sidebar.subheader("🎛 Partner Settings")
            st.sidebar.checkbox("Enable Partner Ads", key="partner_toggle_enable_partner_ads")
            st.sidebar.checkbox("Show Case Study Block", key="partner_toggle_show_case_study")
            st.sidebar.checkbox("Enable Custom CTA", key="partner_toggle_custom_cta")
            st.sidebar.text_input("School Name", key="partner_school_name")

            if st.session_state.get("partner_toggle_custom_cta", False):
                st.sidebar.text_area("CTA Message", key="partner_cta_message")
                st.sidebar.text_input("CTA Button Label", key="partner_cta_button_text")
                st.sidebar.text_input("CTA Link", key="partner_cta_url")
