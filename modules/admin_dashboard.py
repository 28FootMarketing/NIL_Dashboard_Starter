import streamlit as st
from modules.Team_Admin_Panel import role_editor
from modules.toggle_editor import toggle_control_panel
from modals.register_user_modal import register_user_modal
from modules.admin_feedback_viewer import show_feedback_logs
from modules.admin_quick_tools import admin_utilities
from toggles.toggle_flags import load_toggle_flags

# Optional: Restrict full access to internal superadmins only
INTERNAL_ADMINS = ["founder@example.com"]


def admin_dashboard(user_email):
    st.title("🔧 Admin Control Panel")

    if user_email not in INTERNAL_ADMINS:
        st.warning("You have limited admin access.")

    toggle_flags = load_toggle_flags()

    tabs = st.tabs([
        "📊 Dashboard Overview",
        "🔐 Roles & Access",
        "🧰 Feature Toggles",
        "➕ User Registration",
        "📝 Tester Feedback Logs",
        "⚙️ Quick Tools"
    ])

    with tabs[0]:
        st.subheader("📊 System Snapshot")
        st.info("Coming soon: live user/session stats, active toggles, last login")

    with tabs[1]:
        st.subheader("🔐 Role Manager")
        role_editor()

    with tabs[2]:
        st.subheader("🧰 Manage Feature Toggles")
        toggle_control_panel()

    with tabs[3]:
        st.subheader("➕ Manually Register a New User")
        if toggle_flags.get("allow_register", False) or user_email in INTERNAL_ADMINS:
            register_user_modal()
        else:
            st.info("User registration is currently disabled via toggles.")

    with tabs[4]:
        st.subheader("📝 Tester Feedback Logs")
        show_feedback_logs()

    with tabs[5]:
        st.subheader("⚙️ System Tools & Exports")
        admin_utilities()


# Example usage in app.py or main dashboard
# if user_role == "admin":
#     admin_dashboard(user_email=email)
