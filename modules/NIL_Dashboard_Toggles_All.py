import streamlit as st

def dashboard_toggles():
    st.sidebar.header("🛠 Dashboard Toggles")
    enable_dark = st.sidebar.toggle("🌙 Dark Mode", value=True)
    enable_logging = st.sidebar.toggle("📊 Enable Logging", value=True)
    enable_pdf = st.sidebar.toggle("📄 Enable PDF Export", value=True)
    enable_team_mode = st.sidebar.toggle("👥 Enable Team Mode", value=False)
    enable_knowledge_center = st.sidebar.toggle("📚 Show Knowledge Center", value=True)
    
    return {
        "dark_mode": enable_dark,
        "logging": enable_logging,
        "pdf_export": enable_pdf,
        "team_mode": enable_team_mode,
        "knowledge_center": enable_knowledge_center
    }

