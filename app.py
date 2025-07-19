import streamlit as st
from modules.NIL_Dashboard_Toggles_All import show_dashboard
from auth.auth_logic import login, is_logged_in, get_user_role
from auth.auth_logic import reset_password
from modals.register_user_modal import register_user_modal
from auth.auth_logic import get_user_role
from modules.Team_Admin_Panel import role_editor
from modules.NIL_Dashboard_Toggles_All import show_dashboard
# Add any other modules you want to show based on roles

def main():
    st.set_page_config(page_title="NIL Dashboard", layout="wide")

    # Collect login info
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if login(email, password):
        st.success("✅ Login successful")
        user_role = get_user_role()

        # 🔐 Gate Route Logic
        if user_role == "admin":
            st.markdown("### Welcome, Admin 👑")
            show_dashboard()
            role_editor()  # Show role manager UI
            # Add other admin-exclusive tools here

        elif user_role == "coach":
            st.markdown("### Coach Portal 🧢")
            show_dashboard()
            # Add coach tools

        elif user_role == "athlete":
            st.markdown("### Athlete Hub 🏅")
            show_dashboard()
            # Add athlete tools

        else:
            st.warning("🚫 Limited Access")
    else:
        st.warning("❌ Incorrect login. Try again.")
with st.expander("Forgot Password?"):
    reset_email = st.text_input("Email to reset password", key="reset_email")
    new_password = st.text_input("New Password", type="password", key="new_pw")
    
    if st.button("Reset Password"):
        if reset_email and new_password:
            reset_password(reset_email, new_password)
            st.success("✅ Password reset. You can now log in.")
        else:
            st.error("Please fill out both fields.")

def main():
    st.set_page_config(page_title="🏆 NIL Agent Dashboard", layout="wide")

    st.title("🏆 NIL Agent Dashboard")

    # Authentication logic
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(email, password):
            st.success("✅ Login successful")
            role = get_user_role(email)
            show_dashboard(user_role=role)
        else:
            st.error("❌ Invalid email or password")
register_user_modal()

# Optional password reset toggle
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

    if is_logged_in():
        role = get_user_role(email)
        show_dashboard(user_role=role)

if __name__ == "__main__":
    main()
