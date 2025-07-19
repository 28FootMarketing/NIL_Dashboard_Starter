import streamlit as st
import os
import json

from modules.Team_Admin_Panel import role_editor
from modules.toggle_editor import toggle_control_panel
from modals.register_user_modal import register_user_modal
from modules.admin_feedback_viewer import show_feedback_logs
from modules.admin_quick_tools import admin_utilities
from toggles.toggle_flags import load_toggle_flags

# List of emails with full access regardless of toggle settings
INTERNAL_ADMINS = ["founder@example.com"]


def admin_dashboard(user_email: str):
    st.title("🔧 Admin Control Panel")

    # Check internal admin override
    full_access = user_email in INTERNAL_ADMINS
    if not full_access:
        st.warning("You have limited admin access.")

    try:
        toggle_flags = load_toggle_flags()
    except Exception as e:
        st.error(f"Failed to load feature toggles: {e}")
        toggle_flags = {}

    # Define the tab layout
    tabs = st.tabs([
        "📊 Dashboard Overview",
        "🔐 Roles & Access",
        "🧰 Feature Toggles",
        "➕ User Registration",
        "📝 Tester Feedback Logs",
        "⚙️ Quick Tools"
    ])

    # === Overview Tab ===
    with tabs[0]:
        st.subheader("📊 System Snapshot")
        st.info("Live metrics coming soon (users, sessions, logins, active toggles)")

    # === Role Manager Tab ===
    with tabs[1]:
        st.subheader("🔐 Role Manager")
        try:
            role_editor()
        except Exception as e:
            st.error(f"Role editor failed to load: {e}")

    # === Toggle Manager Tab ===
    with tabs[2]:
        st.subheader("🧰 Manage Feature Toggles")
        try:
            toggle_control_panel()
        except Exception as e:
            st.error(f"Toggle panel failed: {e}")

    # === Manual Registration Tab ===
    with tabs[3]:
        st.subheader("➕ Manually Register a New User")
    if toggle_flags.get("allow_register", False) or user_email in INTERNAL_ADMINS:
        register_user_modal()
    else:
        st.info("User registration is currently disabled via toggles.")

    # === Feedback Tab ===
    with tabs[4]:
        st.subheader("📝 Tester Feedback Logs")
        try:
            show_feedback_logs()
        except Exception as e:
            st.error(f"Could not load feedback logs: {e}")

    # === Utilities Tab ===
    with tabs[5]:
        st.subheader("⚙️ System Tools & Exports")
        try:
            admin_utilities()
        except Exception as e:
            st.error(f"Utilities panel failed: {e}")
