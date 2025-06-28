# utils/advertisements.py

import streamlit as st

# Example sponsor mapping
SPONSOR_MAP = {
    "Football": "🏈 Gridiron Performance Labs — Power Your Play.",
    "Basketball": "🏀 CourtVision Eyewear — See the Game Differently.",
    "Track": "👟 SprintFuel Energy Drink — Run Further, Recover Faster.",
    "Default": "📢 NextPlay NIL — Partner with us to feature your brand here.",
}

def show_ad(location="header_ad", sport="Default", partner=None):
    """Renders an ad block based on location, sport, or partner."""
    ad_text = ""

    if partner:
        ad_text = f"🎯 Sponsored by {partner['brand_name']} — {partner['message']}"
    else:
        ad_text = SPONSOR_MAP.get(sport, SPONSOR_MAP["Default"])

    with st.container():
        st.markdown(f"""<div style='padding: 10px; border: 2px solid #ccc; background-color: #f9f9f9;'>
            <strong>{ad_text}</strong>
        </div>""", unsafe_allow_html=True)
