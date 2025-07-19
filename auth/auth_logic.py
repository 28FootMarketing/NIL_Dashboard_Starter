import json
import os

CREDENTIALS_PATH = "data/user_credentials.json"
ROLES_PATH = "data/user_roles.json"

def login(email, password):
    if not os.path.exists(CREDENTIALS_PATH):
        return False
    with open(CREDENTIALS_PATH, "r") as f:
        credentials = json.load(f)
    return credentials.get(email) == password

def is_logged_in(email):
    return email is not None and email != ""

def get_user_role(email):
    if not os.path.exists(ROLES_PATH):
        return None
    with open(ROLES_PATH, "r") as f:
        roles = json.load(f)
    return roles.get(email, "user")

def reset_password(email, new_password):
    if not os.path.exists(CREDENTIALS_PATH):
        return False
    with open(CREDENTIALS_PATH, "r") as f:
        credentials = json.load(f)

    if email not in credentials:
        return False  # Email not found

    credentials[email] = new_password

    with open(CREDENTIALS_PATH, "w") as f:
        json.dump(credentials, f, indent=4)

    return True
