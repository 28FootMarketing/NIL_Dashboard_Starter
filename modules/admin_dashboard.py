import streamlit as st
from modals.register_user_modal import register_user_modal
from modules.Team_Admin_Panel import role_editor
from modules.toggle_editor import toggle_control_panel
import json
import os


def admin_dashboard(user_role):
    st.title("👑 Admin Control Center")

    tab1, tab2, tab3 = st.tabs(["📊 Overview", "🧑‍💼 User Management", "🎛️ Toggles"])

    with tab1:
        st.subheader("📊 System Overview")

        # Load user roles
        role_file = "./data/user_roles.json"
        if os.path.exists(role_file):
            with open(role_file, "r") as f:
                users = json.load(f)

            role_counts = {"admin": 0, "coach": 0, "athlete": 0, "guest": 0}
            for u in users.values():
                role = u.get("role", "guest")
                if role in role_counts:
                    role_counts[role] += 1

            st.metric("Admins", role_counts["admin"])
            st.metric("Coaches", role_counts["coach"])
            st.metric("Athletes", role_counts["athlete"])
            st.metric("Guests", role_counts["guest"])
        else:
            st.info("No user role data found.")

    with tab2:
        st.subheader("🧑‍💼 Manage Users")
        role_editor()
        st.markdown("---")
        register_user_modal()

    with tab3:
        st.subheader("🎛️ Toggle Switchboard")
        toggle_control_panel()

    st.markdown("---")
    st.caption("Only visible to admins. You are logged in as: {}".format(user_role))
