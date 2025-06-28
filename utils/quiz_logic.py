# quiz_logic.py
import streamlit as st

def run_quiz():
    st.write("Answer these 5 quick questions to check your NIL readiness.")

    q1 = st.radio("What grade are you in?", ["9th", "10th", "11th", "12th"])
    q2 = st.radio("Do you have a social media following over 1,000 on any platform?", ["Yes", "No"])
    q3 = st.radio("Have you talked to a coach or mentor about NIL?", ["Yes", "No"])
    q4 = st.radio("Do you currently promote yourself online (e.g., highlights, achievements)?", ["Yes", "No"])
    q5 = st.radio("Are you tracking your stats or brand metrics regularly?", ["Yes", "No"])

    if st.button("Submit Quiz"):
        score = 0
        score += 20 if q1 in ["11th", "12th"] else 10
        score += 20 if q2 == "Yes" else 10
        score += 20 if q3 == "Yes" else 10
        score += 20 if q4 == "Yes" else 10
        score += 20 if q5 == "Yes" else 10
        return score
    return None
