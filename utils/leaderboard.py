# leaderboard.py
import streamlit as st

def display_leaderboard():
    st.markdown("### 🏆 Top NIL Scorers This Week")
    leaderboard_data = [
        {"name": "Ava J.", "score": 95, "school": "East High"},
        {"name": "Miles K.", "score": 90, "school": "West Prep"},
        {"name": "Jordan T.", "score": 88, "school": "North Academy"},
    ]
    for i, entry in enumerate(leaderboard_data, start=1):
        st.write(f"{i}. {entry['name']} – {entry['score']} pts – {entry['school']}")

def earnings_estimator(score):
    return score * 125
