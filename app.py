import streamlit as st
from modules.NIL_Dashboard_Toggles_All import show_dashboard
from auth.auth_logic import login, is_logged_in, get_user_role
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

    if is_logged_in():
        role = get_user_role(email)
        show_dashboard(user_role=role)

if __name__ == "__main__":
    main()
