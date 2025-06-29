import streamlit as st
from utils.partner_config import PartnerConfigHelper

class PartnerDashboard:
    def __init__(self):
        self.config = PartnerConfigHelper.get_config()

    def render(self):
        st.sidebar.title("🤝 Partner Dashboard")
        st.sidebar.markdown(f"**Business Partner:** {self.config.get('business_name', 'N/A')}")
        st.sidebar.markdown("---")

        st.header("📊 Partner Performance Summary")
        st.info(f"✅ Custom CTA Enabled: {'Yes' if self.config.get('custom_cta_enabled') else 'No'}")
        st.info(f"📢 Partner Ads Enabled: {'Yes' if self.config.get('enable_partner_ads') else 'No'}")
        st.info(f"📚 Show Case Study Block: {'Yes' if self.config.get('show_case_study') else 'No'}")

        st.markdown("---")
        st.subheader("📈 Engagement Metrics (Coming Soon)")
        st.markdown("* Total Clicks\n* Leads Generated\n* Campaign ROI\n* Active Templates")

        st.markdown("---")
        st.subheader("🛠 Partner Tools (Planned)")
        st.markdown("* Upload Assets\n* Create Campaigns\n* View Reports")

        st.markdown("---")
        st.caption("Need help? Contact your partner success manager.")
