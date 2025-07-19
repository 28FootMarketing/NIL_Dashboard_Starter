import streamlit as st
import json
import os
import hashlib

USERS_FILE = os.path.join("data", "users.json")
ROLES_FILE = os.path.join("data", "user_roles.json")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


def login(email, password):
    users = load_users()
    hashed = hash_password(password)

    if email in users and users[email]["password"] == hashed:
        st.session_state["is_authenticated"] = True
        st.session_state["user_email"] = email
        st.session_state["user_role"] = get_user_role(email)
        return True
    else:
        st.error("❌ Invalid credentials.")
        return False


def reset_password(email):
    users = load_users()
    if email not in users:
        st.error("❌ Email not found.")
        return False

    new_password = st.text_input("Enter new password", type="password", key="reset_pw_1")
    confirm_password = st.text_input("Confirm new password", type="password", key="reset_pw_2")

    if st.button("Update Password"):
        if new_password and new_password == confirm_password:
            users[email]["password"] = hash_password(new_password)
            save_users(users)
            st.success("✅ Password updated successfully.")
            return True
        else:
            st.error("❌ Passwords do not match.")
    return False


def is_logged_in():
    return st.session_state.get("is_authenticated", False)


def logout():
    st.session_state.clear()
    st.success("🔒 Logged out successfully.")


def get_user_role(email):
    if not os.path.exists(ROLES_FILE):
        return "guest"
    with open(ROLES_FILE, "r") as f:
        roles = json.load(f)
    return roles.get(email, "guest")
