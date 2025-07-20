import streamlit as st
import os
import json

from modules.Team_Admin_Panel import role_editor
from modules.toggle_editor import toggle_control_panel
from modals.register_user_modal import register_user_modal
from modules.admin_feedback_viewer import show_feedback_logs
from modules.admin_quick_tools import admin_utilities
from toggles.toggle_flags import load_toggle_flags
from utils.audit_logger import log_event  # ✅ Logging added

INTERNAL_ADMINS = ["founder@example.com"]

def admin_dashboard(user_email: str):
    st.title("🔧 Admin Control Panel")

    full_access = user_email in INTERNAL_ADMINS
    if not full_access:
        st.warning("You have limited admin access.")
        log_event(user_email, "Accessed Admin Dashboard (Limited Access)")
    else:
        log_event(user_email, "Accessed Admin Dashboard (Full Access)")

    try:
        toggle_flags = load_toggle_flags()
    except Exception as e:
        st.error(f"Failed to load feature toggles: {e}")
        toggle_flags = {}

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
        st.info("Live metrics coming soon (users, sessions, logins, active toggles)")
        log_event(user_email, "Viewed: Dashboard Overview")

    with tabs[1]:
        st.subheader("🔐 Role Manager")
        try:
            role_editor()
            log_event(user_email, "Opened Role & Access Manager")
        except Exception as e:
            st.error(f"Role editor failed to load: {e}")

    with tabs[2]:
        st.subheader("🧰 Manage Feature Toggles")
        try:
            toggle_control_panel()
            log_event(user_email, "Accessed Toggle Editor")
        except Exception as e:
            st.error(f"Toggle panel failed: {e}")

    with tabs[3]:
        st.subheader("➕ Manually Register a New User")
        if toggle_flags.get("allow_register", False) or full_access:
            try:
                register_user_modal()
                log_event(user_email, "Opened User Registration Modal")
            except Exception as e:
                st.error(f"Registration modal failed: {e}")
        else:
            st.info("User registration is currently disabled via toggles.")
            log_event(user_email, "Attempted Registration Access (Disabled)")

    with tabs[4]:
        st.subheader("📝 Tester Feedback Logs")
        try:
            show_feedback_logs()
            log_event(user_email, "Viewed Tester Feedback Logs")
        except Exception as e:
            st.error(f"Could not load feedback logs: {e}")

    with tabs[5]:
        st.subheader("⚙️ System Tools & Exports")
        try:
            admin_utilities()
            log_event(user_email, "Accessed Admin Quick Tools")
        except Exception as e:
            st.error(f"Utilities panel failed: {e}")
