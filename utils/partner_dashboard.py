import streamlit as st
from utils.partner_config import PartnerConfigHelper

class PartnerDashboard:
    def __init__(self):
        # Load all configs once
        self.configs = PartnerConfigHelper.load_configs()

        # Initialize session state for selected partner
        if "selected_partner_id" not in st.session_state:
            st.session_state["selected_partner_id"] = "default_partner"

        self.partner_id = st.session_state["selected_partner_id"]
        self.config = self.configs.get(self.partner_id, PartnerConfigHelper.get_config())

    def render(self):
        with st.sidebar:
            st.title("🤝 Partner Dashboard")

            # Partner switcher
            partner_options = list(self.configs.keys())
            selected = st.selectbox("🔁 Switch Partner", partner_options, index=partner_options.index(self.partner_id))
            if selected != self.partner_id:
                st.session_state["selected_partner_id"] = selected
                st.experimental_rerun()

            st.markdown(f"**Brand Name:** `{self.config.get('brand_name', 'N/A')}`")
            st.markdown(f"**Tagline:** {self.config.get('tagline', 'N/A')}")
            st.markdown("---")

        st.header(f"📊 Performance Summary for {self.config.get('brand_name', 'N/A')}")

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
