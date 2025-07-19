# modules/NIL_Dashboard_Toggles_All.py

import streamlit as st
from datetime import datetime

def show_dashboard(user_role="guest", timezone="US/Eastern"):
    st.markdown("## 🧠 NIL Analytics Dashboard")

    # 🌍 Show Date/Time Based on Timezone
    local_time = datetime.now().astimezone().strftime('%A, %B %d, %Y — %I:%M %p')
    st.markdown(f"**Current Time:** {local_time}")

    # 🧩 Dashboard Toggles
    st.sidebar.subheader("📌 Dashboard Toggles")
    show_ai_response = st.sidebar.toggle("Show AI Response", value=True)
    show_summary_charts = st.sidebar.toggle("Show Summary Charts", value=True)
    show_team_tab = st.sidebar.toggle("Enable Team Mode", value=False)
    show_pdf_export = st.sidebar.toggle("Enable PDF Export", value=False)
    show_knowledge_tab = st.sidebar.toggle("Enable Knowledge Tab", value=False)
    dark_mode_enabled = st.sidebar.toggle("Dark Mode", value=False)

    # 🔧 Output: Config Dict
    toggles = {
        "show_ai_response": show_ai_response,
        "show_summary_charts": show_summary_charts,
        "show_team_tab": show_team_tab,
        "show_pdf_export": show_pdf_export,
        "show_knowledge_tab": show_knowledge_tab,
        "dark_mode_enabled": dark_mode_enabled,
        "user_role": user_role
    }

    st.session_state["dashboard_toggles"] = toggles

    # 🧪 Optional preview (dev only)
    with st.expander("🧪 Toggle Debug View"):
        st.json(toggles)
