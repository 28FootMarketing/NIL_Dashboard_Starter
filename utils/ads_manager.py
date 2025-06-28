# utils/ads_manager.py

import streamlit as st

ADS = {
    "header_ad": {
        "type": "image",
        "src": "https://example.com/ad_header.jpg",
        "link": "https://sponsor-site.com",
        "alt": "Sponsor Header Ad"
    },
    "sidebar_ad": {
        "type": "text",
        "content": "**🔥 Partner Offer:** Get 20% off your NIL merch at [ShopNIL.com](https://shopnil.com)",
    },
    "footer_ad": {
        "type": "html",
        "content": "<div style='background:#222;padding:10px;color:white;text-align:center;'>📣 Powered by <a href='https://nextplaypartners.com' target='_blank'>NextPlay Partners</a></div>"
    }
}

def show_ad(slot):
    ad = ADS.get(slot)
    if not ad:
        return

    if ad["type"] == "image":
        st.markdown(f"[![{ad['alt']}]({ad['src']})]({ad['link']})", unsafe_allow_html=True)
    elif ad["type"] == "text":
        st.markdown(ad["content"], unsafe_allow_html=True)
    elif ad["type"] == "html":
        st.components.v1.html(ad["content"], height=60)

