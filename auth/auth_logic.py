import json
import os

CRED_FILE = os.path.join("data", "user_credentials.json")
ROLE_FILE = os.path.join("data", "user_roles.json")


def register_user(email, password, role="guest"):
    email = email.strip().lower()

    # Load or initialize credential store
    if os.path.exists(CRED_FILE):
        with open(CRED_FILE, "r") as f:
            credentials = json.load(f)
    else:
        credentials = {}

    if os.path.exists(ROLE_FILE):
        with open(ROLE_FILE, "r") as f:
            roles = json.load(f)
    else:
        roles = {}

    # Check for existing account
    if email in credentials:
        return False, "User already exists."

    # Add new user
    credentials[email] = {"password": password}
    roles[email] = {"role": role}

    # Save changes
    with open(CRED_FILE, "w") as f:
        json.dump(credentials, f, indent=2)

    with open(ROLE_FILE, "w") as f:
        json.dump(roles, f, indent=2)

    return True, "User registered successfully."
