import streamlit as st
from modules.NIL_Dashboard_Toggles_All import show_dashboard
from auth.auth_logic import login, is_logged_in, get_user_role, reset_password
from modals.register_user_modal import register_user_modal
from modules.Team_Admin_Panel import role_editor
from toggles.toggle_flags import load_toggle_flags
from modules.toggle_editor import toggle_control_panel


def main():
    st.set_page_config(page_title="🏆 NIL Agent Dashboard", layout="wide")
    st.title("🏆 NIL Agent Dashboard")

    # Load toggle settings
    toggle_flags = load_toggle_flags()

    # Login Fields
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not email or not password:
            st.error("Email and password are required.")
            return

        if login(email, password):
            st.success("✅ Login successful")
            user_role = get_user_role(email)
            st.session_state["authenticated"] = True
            st.session_state["user_email"] = email
            st.session_state["user_role"] = user_role

            # 🔐 Gate Route Logic
            if user_role == "admin":
                st.markdown("### Welcome, Admin 👑")
                show_dashboard(user_role=user_role)
                role_editor()
                toggle_control_panel(user_role)  # Secured toggle panel
                if toggle_flags.get("allow_register", False):
                    register_user_modal()

            elif user_role == "coach":
                st.markdown("### Coach Portal 🧢")
                show_dashboard(user_role=user_role)

            elif user_role == "athlete":
                st.markdown("### Athlete Hub 🏅")
                show_dashboard(user_role=user_role)

            else:
                st.error("🚫 Access Denied")
                st.markdown("Your role does not grant access to this dashboard.")
                st.session_state["authenticated"] = False
                st.experimental_rerun()
        else:
            st.error("❌ Invalid email or password")

    # Optional Password Reset Section
    with st.expander("🔑 Forgot your password? Reset it here"):
        reset_email = st.text_input("Reset Email", key="reset_email_modal")
        new_pass = st.text_input("New Password", type="password", key="new_pass")
        confirm_pass = st.text_input("Confirm New Password", type="password", key="confirm_pass")

        if st.button("Reset Password", key="reset_btn"):
            if not reset_email or not new_pass or not confirm_pass:
                st.error("Please fill in all fields.")
            elif new_pass != confirm_pass:
                st.error("Passwords do not match.")
            else:
                success = reset_password(reset_email, new_pass)
                if success:
                    st.success("Password reset successfully. Please log in with your new credentials.")
                else:
                    st.error("Something went wrong. Try again or contact support.")


if __name__ == "__main__":
    main()
