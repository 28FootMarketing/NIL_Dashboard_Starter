import json
import os
import streamlit as st

# File paths
CRED_FILE = "./data/user_credentials.json"
ROLE_FILE = "./data/user_roles.json"

# Load credentials from JSON
def load_credentials():
    if os.path.exists(CRED_FILE):
        with open(CRED_FILE, "r") as f:
            return json.load(f)
    return {}

# Save credentials to JSON
def save_credentials(creds):
    with open(CRED_FILE, "w") as f:
        json.dump(creds, f, indent=2)

# Load roles from JSON
def load_roles():
    if os.path.exists(ROLE_FILE):
        with open(ROLE_FILE, "r") as f:
            return json.load(f)
    return {}

# Get the user's assigned role
def get_user_role(email):
    roles = load_roles()
    return roles.get(email, "guest")

# Login function
def login(email, password):
    creds = load_credentials()
    if email in creds and creds[email] == password:
        st.session_state["logged_in"] = True
        st.session_state["email"] = email
        st.session_state["user_role"] = get_user_role(email)
        return True
    return False

# Check if user is logged in
def is_logged_in():
    return st.session_state.get("logged_in", False)

# Password reset
def reset_password(email, new_password):
    creds = load_credentials()
    creds[email] = new_password
    save_credentials(creds)
    return True
