import streamlit as st
import json
import os

# Load roles from local file
def load_roles():
    path = "data/user_roles.json"
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

# Simulated login (email + password combo)
def login(email, password):
    roles = load_roles()
    if email in roles:
        if password == "password123":  # Dev-only fallback password
            st.session_state["logged_in"] = True
            st.session_state["email"] = email
            st.session_state["role"] = roles[email]
            return True
    return False

# Check session login state
def is_logged_in():
    return st.session_state.get("logged_in", False)

# Get current user role
def get_user_role():
    return st.session_state.get("role", "guest")

# Logout helper
def logout():
    st.session_state.clear()
