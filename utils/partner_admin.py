import streamlit as st
from utils.partner_config import PartnerConfigHelper
from utils.logger import log_change

def show_partner_admin():
    st.header("🔧 White-Label Partner Manager")

    configs = PartnerConfigHelper.load_configs()
    if not configs:
        st.warning("⚠️ No partner configurations found.")
        return

    selected = st.selectbox("Choose Partner", list(configs.keys()))
    current = configs[selected]

    form_key = f"partner_form_{selected}"
    with st.form(key=form_key):
        brand_key = f"brand_name_{selected}"
        tagline_key = f"tagline_{selected}"
        color_key = f"primary_color_{selected}"
        logo_key = f"logo_url_{selected}"
        email_key = f"contact_email_{selected}"

        st.subheader("🪪 Branding Info")
        st.text_input("Brand Name", value=current["brand_name"], key=brand_key)
        st.text_input("Tagline", value=current["tagline"], key=tagline_key)
        st.color_picker("Primary Color", value=current["primary_color"], key=color_key)
        st.text_input("Logo URL", value=current["logo_url"], key=logo_key)
        st.text_input("Contact Email", value=current["contact_email"], key=email_key)

        st.subheader("🧩 Feature Toggles")
        pitch = st.checkbox("✅ Pitch Deck", value=current["features"].get("pitch_deck", False), key=f"pitch_{selected}")
        deal = st.checkbox("✅ Deal Builder", value=current["features"].get("deal_builder", False), key=f"deal_{selected}")
        contract = st.checkbox("✅ Contract PDF", value=current["features"].get("contract_pdf", False), key=f"contract_{selected}")
        admin = st.checkbox("✅ Admin Tools", value=current["features"].get("admin_tools", False), key=f"admin_{selected}")

        submit = st.form_submit_button("💾 Save Changes")

    if submit:
        updated_config = {
            "brand_name": st.session_state[brand_key],
            "tagline": st.session_state[tagline_key],
            "primary_color": st.session_state[color_key],
            "logo_url": st.session_state[logo_key],
            "contact_email": st.session_state[email_key],
            "features": {
                "pitch_deck": pitch,
                "deal_builder": deal,
                "contract_pdf": contract,
                "admin_tools": admin
            }
        }

        PartnerConfigHelper.save_config(selected, updated_config)
        log_change(f"Updated config for partner: {selected}", actor="Admin")
        st.success(f"✅ Partner '{selected}' updated successfully.")
