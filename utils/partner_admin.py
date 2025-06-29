# utils/partner_admin.py

import streamlit as st
import json
from utils.partner_config import PartnerConfigHelper  # ✅ Updated import

def show_partner_admin():
    st.header("🔧 White-Label Partner Manager")

    configs = PartnerConfigHelper.load_configs()  # ✅ Load current configs
    selected = st.selectbox("Choose Partner", list(configs.keys()))
    current = configs[selected]

    st.text_input("Brand Name", value=current["brand_name"], key="brand_name")
    st.text_input("Tagline", value=current["tagline"], key="tagline")
    st.color_picker("Primary Color", value=current["primary_color"], key="primary_color")
    st.text_input("Logo URL", value=current["logo_url"], key="logo_url")
    st.text_input("Contact Email", value=current["contact_email"], key="contact_email")

    with st.expander("Feature Toggles"):
        pitch = st.checkbox("Pitch Deck", value=current["features"]["pitch_deck"], key="pitch")
        deal = st.checkbox("Deal Builder", value=current["features"]["deal_builder"], key="deal")
        contract = st.checkbox("Contract PDF", value=current["features"]["contract_pdf"], key="contract")
        admin = st.checkbox("Admin Tools", value=current["features"]["admin_tools"], key="admin")

    if st.button("💾 Save Changes"):
        updated = {
            "brand_name": st.session_state.brand_name,
            "tagline": st.session_state.tagline,
            "primary_color": st.session_state.primary_color,
            "logo_url": st.session_state.logo_url,
            "contact_email": st.session_state.contact_email,
            "features": {
                "pitch_deck": pitch,
                "deal_builder": deal,
                "contract_pdf": contract,
                "admin_tools": admin
            }
        }
        PartnerConfigHelper.save_config(selected, updated)  # ✅ Use class method
        st.success(f"✅ Partner '{selected}' updated.")
