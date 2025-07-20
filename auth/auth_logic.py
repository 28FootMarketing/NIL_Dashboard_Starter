import json
import os

USER_DB = "./data/user_roles.json"

def load_user_data():
    if os.path.exists(USER_DB):
        with open(USER_DB, "r") as f:
            return json.load(f)
    return {}

def save_user_data(data):
    with open(USER_DB, "w") as f:
        json.dump(data, f, indent=4)

def login(email, password):
    users = load_user_data()
    user = users.get(email)
    return user and user.get("password") == password

def is_logged_in(email):
    users = load_user_data()
    return email in users

def get_user_role(email):
    users = load_user_data()
    return users.get(email, {}).get("role", "guest")

def reset_password(email, new_password):
    users = load_user_data()
    if email in users:
        users[email]["password"] = new_password
        save_user_data(users)
        return True
    return False
