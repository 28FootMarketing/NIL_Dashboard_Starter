# utils/partner_admin.py

import streamlit as st
import json


def show_partner_admin():
    st.header("🔧 White-Label Partner Manager")

    selected = st.selectbox("Choose Partner", list(PARTNER_CONFIGS.keys()))
    current = PARTNER_CONFIGS[selected]

    st.text_input("Brand Name", current["brand_name"], key="brand_name")
    st.text_input("Tagline", current["tagline"], key="tagline")
    st.color_picker("Primary Color", current["primary_color"], key="primary_color")
    st.text_input("Logo URL", current["logo_url"], key="logo_url")
    st.text_input("Contact Email", current["contact_email"], key="contact_email")

    with st.expander("Feature Toggles"):
        pitch = st.checkbox("Pitch Deck", current["features"]["pitch_deck"], key="pitch")
        deal = st.checkbox("Deal Builder", current["features"]["deal_builder"], key="deal")
        contract = st.checkbox("Contract PDF", current["features"]["contract_pdf"], key="contract")
        admin = st.checkbox("Admin Tools", current["features"]["admin_tools"], key="admin")

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
        save_partner_config(selected, updated)
        st.success(f"✅ Partner '{selected}' updated.")


def save_partner_config(partner_id, updated_config):
    try:
        with open("utils/partner_configs.json", "r") as f:
            configs = json.load(f)
    except FileNotFoundError:
        configs = {}

    configs[partner_id] = updated_config

    with open("utils/partner_configs.json", "w") as f:
        json.dump(configs, f, indent=2)
