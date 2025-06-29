# utils/partner_branding.py
import streamlit as st
from utils.logger import log_change

def show_brand_preview_panel(partner_config):
    st.subheader("🎨 Partner Branding Preview")

    col1, col2 = st.columns([1, 2])

    with col1:
        logo = st.file_uploader("Upload Logo (PNG/JPG)", type=["png", "jpg"])
        if logo:
            st.image(logo, width=120)
            st.session_state["partner_logo"] = logo
            log_change("Updated partner logo", actor="Admin")

    with col2:
        tagline = st.text_input("Partner Tagline", value=partner_config.get("tagline", "Empowering NIL Athletes"))
        if tagline != partner_config.get("tagline"):
            partner_config["tagline"] = tagline
            log_change(f"Updated tagline to: {tagline}", actor="Admin")

        primary_color = st.color_picker("Primary Theme Color", value=partner_config.get("color", "#0044cc"))
        if primary_color != partner_config.get("color"):
            partner_config["color"] = primary_color
            log_change(f"Updated theme color to: {primary_color}", actor="Admin")

    st.markdown("---")
    st.markdown(f"#### Preview")
    st.markdown(f"""
    <div style='border: 2px solid {partner_config.get("color", "#0044cc")}; padding: 1rem; border-radius: 10px;'>
        <h3 style='color: {partner_config.get("color", "#0044cc")};'>{partner_config.get("tagline", "Your NIL Partner")}</h3>
        <p>This is how your partner message will look inside app sections.</p>
    </div>
    """, unsafe_allow_html=True)
