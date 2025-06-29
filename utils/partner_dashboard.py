import streamlit as st
from utils.partner_config import PartnerConfigHelper

class PartnerDashboard:
    def __init__(self, partner_id="default_partner"):
        self.config = PartnerConfigHelper.get_config(partner_id)
        self.partner_id = partner_id

    def render(self):
        st.sidebar.title("🤝 Partner Dashboard")
        st.sidebar.markdown(f"**Partner ID:** `{self.partner_id}`")
        st.sidebar.markdown(f"**Business Partner:** {self.config.get('brand_name', 'N/A')}")
        st.sidebar.markdown("---")

        st.header(f"📊 {self.config.get('brand_name', 'Partner')} Performance Summary")

        st.info(f"✅ Custom CTA Enabled: {'Yes' if self.config.get('custom_cta_enabled', False) else 'No'}")
        st.info(f"📢 Partner Ads Enabled: {'Yes' if self.config.get('enable_partner_ads', False) else 'No'}")
        st.info(f"📚 Show Case Study Block: {'Yes' if self.config.get('show_case_study', False) else 'No'}")

        st.markdown("---")
        st.subheader("📈 Engagement Metrics (🚧 Coming Soon)")
        st.markdown("""
        * ✅ Total Clicks  
        * ⌛ Leads Generated  
        * 🚧 Campaign ROI  
        * 🚧 Active Templates  
        """)

        st.markdown("---")
        st.subheader("🛠 Partner Tools (Planned)")
        st.markdown("""
        * ⌛ Upload Assets  
        * 🚧 Create Campaigns  
        * ⌛ View Reports  
        """)

        st.markdown("---")
        st.caption("Need help? Contact your partner success manager or email support.")
