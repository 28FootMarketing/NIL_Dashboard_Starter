# File: modules/admin_quick_tools.py

import streamlit as st

def admin_utilities():
    st.subheader("⚙️ Quick Admin Tools")

    # Example utility buttons (extend as needed)
    if st.button("🔄 Refresh Dashboard"):
        st.success("Dashboard refreshed!")

    if st.button("📤 Export All Logs"):
        st.info("Log export feature coming soon.")

    if st.button("🧪 Trigger Test Action"):
        st.warning("This is a test action.")
