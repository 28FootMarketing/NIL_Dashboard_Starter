import json
import os
import streamlit as st
import hashlib

USER_DB_FILE = "data/user_db.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_user_db():
    if not os.path.exists(USER_DB_FILE):
        return {}
    with open(USER_DB_FILE, "r") as file:
        return json.load(file)

def save_user_db(db):
    with open(USER_DB_FILE, "w") as file:
        json.dump(db, file, indent=4)

def register_user(email, password, role="user"):
    db = load_user_db()

    if email in db:
        return {"success": False, "error": "User already exists."}

    db[email] = {
        "password": hash_password(password),
        "role": role
    }
    save_user_db(db)
    return {"success": True, "message": "Registration successful."}
# auth_logic.py

def login(email, password):
    # login logic
    return True

def is_logged_in():
    return True

def get_user_role(email=None):
    return "admin"

def reset_password(email, new_password):
    return True
