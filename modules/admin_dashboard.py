import streamlit as st
from modules.NIL_Dashboard_Toggles_All import show_dashboard
from modules.Team_Admin_Panel import role_editor
from modules.toggle_editor import toggle_control_panel
from modals.register_user_modal import register_user_modal
from toggles.toggle_flags import load_toggle_flags

def render_admin_dashboard():
    st.title("👑 Admin Control Center")
    st.markdown("Welcome, Administrator. Use the panels below to manage system features and users.")

    # Section 1: Dashboard Preview
    with st.expander("📊 NIL Dashboard Overview"):
        show_dashboard(user_role="admin")

    # Section 2: Role & Access Management
    with st.expander("🔐 Manage User Roles"):
        st.info("Edit user roles (admin, coach, athlete, guest) to control access.")
        role_editor()

    # Section 3: Feature Toggles
    with st.expander("🧰 System Feature Toggles"):
        st.info("Enable or disable key features using toggle switches below.")
        toggle_control_panel()

    # Section 4: Manual Registration (if toggle allows)
    toggle_flags = load_toggle_flags()
    if toggle_flags.get("allow_register", False):
        with st.expander("➕ Manual User Registration"):
            st.info("Register new users directly from the admin panel.")
            register_user_modal()
