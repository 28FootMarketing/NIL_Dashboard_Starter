# File: modules/admin_quick_tools.py

import streamlit as st
import json
import os
from toggles.toggle_flags import save_toggle_flags, load_toggle_flags

USER_ROLE_PATH = "./data/user_roles.json"
TOGGLE_PATH = "./toggles/toggles.json"

def admin_utilities():
    st.subheader("⚙️ Quick Admin Tools")

    # 🔄 Refresh Dashboard
    if st.button("🔁 Force Rerun"):
        st.success("Dashboard will reload.")
        st.experimental_rerun()

    # 📤 Export All User Roles
    if st.button("📤 Export User Roles as JSON"):
        if os.path.exists(USER_ROLE_PATH):
            with open(USER_ROLE_PATH, "r") as f:
                st.download_button("⬇️ Download user_roles.json", f.read(), file_name="user_roles.json", mime="application/json")
        else:
            st.error("User roles file not found.")

    # 🔧 Toggle Reset Option
    if st.button("🔃 Reset Toggle Flags to Default"):
        default_flags = {
            "allow_register": True,
            "allow_feedback": True,
            "maintenance_mode": False
        }
        save_toggle_flags(default_flags)
        st.success("Toggles reset to default.")

    # 🔍 View Current Toggles
    with st.expander("📊 View Current Toggle Flags"):
        current_flags = load_toggle_flags()
        st.json(current_flags)

    # 🔐 Lock All Roles to Guest
    if st.button("🔒 Lock All Roles to Guest"):
        if os.path.exists(USER_ROLE_PATH):
            with open(USER_ROLE_PATH, "r") as f:
                data = json.load(f)
            for email in data:
                data[email]["role"] = "guest"
            with open(USER_ROLE_PATH, "w") as f:
                json.dump(data, f, indent=4)
            st.warning("All users have been downgraded to guest.")
        else:
            st.error("User roles file not found.")
