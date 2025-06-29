import streamlit as st
from utils.partner_config import PartnerConfigHelper
from utils.logger import log_change
from utils.admin_tools import check_admin_access

def show_partner_admin():
    if not check_admin_access():
        st.warning("🚫 You do not have permission to view this panel.")
        return

    st.header("🔧 White-Label Partner Manager")

    configs = PartnerConfigHelper.load_configs()
    if not configs:
        st.warning("⚠️ No partner configurations found.")
        return

    selected = st.selectbox("Choose Partner", list(configs.keys()))
    current = configs[selected]

    brand_key = f"brand_name_{selected}"
    tagline_key = f"tagline_{selected}"
    color_key = f"primary_color_{selected}"
    logo_key = f"logo_url_{selected}"
    email_key = f"contact_email_{selected}"
    tier_key = f"partner_tier_{selected}"

    pitch_key = f"pitch_{selected}"
    deal_key = f"deal_{selected}"
    contract_key = f"contract_{selected}"
    admin_key = f"admin_{selected}"

    form_key = f"partner_form_{selected}"
    with st.form(key=form_key):
        st.subheader("🪪 Branding Info")
        st.text_input("Brand Name", value=current["brand_name"], key=brand_key)
        st.text_input("Tagline", value=current["tagline"], key=tagline_key)
        st.color_picker("Primary Color", value=current["primary_color"], key=color_key)
        st.text_input("Logo URL", value=current["logo_url"], key=logo_key)
        st.text_input("Contact Email", value=current["contact_email"], key=email_key)
        st.selectbox(
            "Partner Tier",
            ["Bronze", "Silver", "Gold"],
            index=["Bronze", "Silver", "Gold"].index(current.get("partner_tier", "Bronze")),
            key=tier_key
        )

        st.subheader("🧩 Feature Toggles")
        st.checkbox("✅ Pitch Deck", value=current["features"].get("pitch_deck", False), key=pitch_key)
        st.checkbox("✅ Deal Builder", value=current["features"].get("deal_builder", False), key=deal_key)
        st.checkbox("✅ Contract PDF", value=current["features"].get("contract_pdf", False), key=contract_key)
        st.checkbox("✅ Admin Tools", value=current["features"].get("admin_tools", False), key=admin_key)

        submitted = st.form_submit_button("💾 Save Changes")

    if submitted:
        updated = {
            "brand_name": st.session_state[brand_key],
            "tagline": st.session_state[tagline_key],
            "primary_color": st.session_state[color_key],
            "logo_url": st.session_state[logo_key],
            "contact_email": st.session_state[email_key],
            "partner_tier": st.session_state[tier_key],
            "features": {
                "pitch_deck": st.session_state[pitch_key],
                "deal_builder": st.session_state[deal_key],
                "contract_pdf": st.session_state[contract_key],
                "admin_tools": st.session_state[admin_key]
            }
        }

        PartnerConfigHelper.save_config(selected, updated)
        log_change(f"✅ Partner config saved for: {selected}", actor="Admin")
        st.success(f"✅ Partner '{selected}' updated successfully.")

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("✏️ Edit Partner Settings Again"):
            st.rerun()

    with col2:
        if st.button(f"🗑️ Delete '{selected}'", key=f"delete_{selected}"):
            confirm = st.radio(
                f"Confirm delete for '{selected}'?",
                ["No", "Yes, delete permanently"],
                index=0,
                key=f"confirm_delete_{selected}"
            )
            if confirm == "Yes, delete permanently":
                del configs[selected]
                PartnerConfigHelper.save_config(selected=None, config_data=configs)
                log_change(f"🗑️ Partner deleted: {selected}", actor="Admin")
                st.warning(f"Partner '{selected}' has been deleted. Please refresh.")
                st.stop()
