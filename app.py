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

    # 🔁 Load toggle flags (controls admin features)
    toggle_flags = load_toggle_flags()

    # 🔐 Already authenticated session
    if st.session_state.get("authenticated"):
        user_email = st.session_state.get("user_email", "")
        user_role = get_user_role(user_email)

        st.success(f"✅ Logged in as {user_email} ({user_role})")

        # 🚪 Logout button (visible after login)
        if st.button("🚪 Logout"):
            st.session_state["authenticated"] = False
            st.session_state["user_email"] = ""
            st.experimental_rerun()

        # Role-based dashboards
        if user_role == "admin":
            st.markdown("### Welcome, Admin 👑")
            show_dashboard(user_role=user_role)
            role_editor()
            toggle_control_panel()

            if toggle_flags.get("allow_register", False):
                register_user_modal()

        elif user_role == "coach":
            st.markdown("### Coach Portal 🧢")
            show_dashboard(user_role=user_role)

        elif user_role == "athlete":
            st.markdown("### Athlete Hub 🏅")
            show_dashboard(user_role=user_role)

        else:
            st.error("🚫 Invalid role. Access denied.")
            st.session_state["authenticated"] = False
            st.stop()

        st.stop()  # Prevent login form from appearing again

    # 🔑 Login Form
    st.subheader("Login to Your NIL Dashboard")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not email or not password:
            st.error("Email and password are required.")
            st.stop()

        if login(email, password):
            st.success("✅ Login successful")
            st.session_state["authenticated"] = True
            st.session_state["user_email"] = email
            st.experimental_rerun()
        else:
            st.error("❌ Invalid email or password")

    # 📝 Optional: Registration form (admin-controlled via toggle)
    if toggle_flags.get("allow_register", False):
        st.markdown("---")
        st.subheader("📋 Admin Registration")
        register_user_modal()

    # 🔁 Password Reset
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
