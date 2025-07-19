import streamlit as st
from datetime import datetime

def show_admin_panel():
    st.header("🧑‍💼 Team Admin Panel")
    
    st.markdown("### Team Activity Log")
    st.dataframe([
        {"Athlete": "Maliyah", "Query": "Can I sell merch?", "Timestamp": datetime.now()},
        {"Athlete": "Tyson", "Query": "Florida NIL laws", "Timestamp": datetime.now()}
    ])
    
    st.markdown("### Manage Access")
    st.text_input("Invite new team member")
    st.button("Send Invite")

    st.markdown("### System Toggles")
    st.checkbox("Enable Real-time Logging", value=True)
    st.checkbox("Show Knowledge Center", value=True)
