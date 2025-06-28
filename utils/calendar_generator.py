# calendar_generator.py
import streamlit as st

def display_calendar():
    st.markdown("### 📅 Weekly NIL Content Plan")
    st.write("Here’s a simple layout for your weekly posts:")
    calendar = {
        "Monday": "Highlight your top play or stat.",
        "Wednesday": "Post a workout or training clip.",
        "Friday": "Shoutout a brand or local sponsor.",
        "Sunday": "Reflect on your week or share goals."
    }
    for day, post in calendar.items():
        st.write(f"**{day}**: {post}")
