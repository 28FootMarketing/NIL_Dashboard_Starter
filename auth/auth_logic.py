import json
import os

CRED_FILE = "./data/user_credentials.json"

def load_credentials():
    if os.path.exists(CRED_FILE):
        with open(CRED_FILE, "r") as f:
            return json.load(f)
    return {}

def save_credentials(creds):
    with open(CRED_FILE, "w") as f:
        json.dump(creds, f, indent=2)

def login(email, password):
    creds = load_credentials()
    if email in creds and creds[email] == password:
        st.session_state["logged_in"] = True
        st.session_state["email"] = email
        return True
    return False

def reset_password(email, new_password):
    creds = load_credentials()
    creds[email] = new_password
    save_credentials(creds)
    return True
