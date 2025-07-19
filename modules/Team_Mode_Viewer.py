import streamlit as st
import pandas as pd

def display_team_mode(session_log_df):
    st.markdown("## 👥 Team Session Viewer")
    
    coach_id = st.text_input("Enter Coach/Org ID", "")
    if coach_id:
        filtered_df = session_log_df[session_log_df["coach_id"] == coach_id]
        st.dataframe(filtered_df)
    else:
        st.info("Enter a valid Coach/Org ID to view team sessions.")

