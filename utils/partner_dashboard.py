# utils/partner_dashboard.py

import streamlit as st

class PartnerDashboard:
    def __init__(self):
        self._initialize_defaults()

    def _initialize_defaults(self):
        defaults = {
            "partner_business_name": "Your Business",
            "partner_toggle_enable_partner_ads": False,
            "partner_toggle_show_case_study": False,
            "partner_toggle_custom_cta": False,
            "partner_campaign_clicks": 0,
            "partner_leads_collected": 0,
            "partner_ad_impressions": 0
        }
        for key, val in defaults.items():
            if key not in st.session_state or type(st.session_state[key]) != type(val):
                st.session_state[key] = val

    def render(self):
        st.sidebar.subheader("🎯 Partner Dashboard")

        st.sidebar.text_input("Business Name", key="partner_business_name")
        st.sidebar.checkbox("Enable Partner Ads", key="partner_toggle_enable_partner_ads")
        st.sidebar.checkbox("Show Case Study Block", key="partner_toggle_show_case_study")
        st.sidebar.checkbox("Enable Custom CTA", key="partner_toggle_custom_cta")

        st.sidebar.markdown("---")
        st.sidebar.markdown("### 📊 Performance Snapshot")
        st.sidebar.metric("Ad Impressions", st.session_state["partner_ad_impressions"])
        st.sidebar.metric("Leads Collected", st.session_state["partner_leads_collected"])
        st.sidebar.metric("Campaign Clicks", st.session_state["partner_campaign_clicks"])

        st.sidebar.markdown("---")
        if st.button("🔄 Reset Partner Stats"):
            st.session_state["partner_ad_impressions"] = 0
            st.session_state["partner_leads_collected"] = 0
            st.session_state["partner_campaign_clicks"] = 0
