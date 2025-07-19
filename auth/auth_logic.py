import streamlit as st
from auth.auth_config import supabase

def login(email, password):
    result = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })
    st.session_state.user = result.user

def is_logged_in():
    return "user" in st.session_state

def get_user_role(email):
    # Pull from Supabase or local JSON
    return "coach" if email.endswith("@school.org") else "athlete"
