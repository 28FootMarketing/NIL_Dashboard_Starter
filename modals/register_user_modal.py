import streamlit as st
from auth.auth_logic import register_user

def register_user_modal():
    st.markdown("### ➕ Register a New User")

    with st.form("register_user_form", clear_on_submit=False):
        email = st.text_input("Email Address").strip().lower()
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        roles = ["admin", "coach", "athlete", "guest"]
        role = st.selectbox("Assign Role", roles)

        submitted = st.form_submit_button("Register User")

        if submitted:
            # Basic validation
            if not email:
                st.error("Email is required.")
            elif len(password) < 8:
                st.error("Password must be at least 8 characters.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            elif role not in roles:
                st.error("Invalid role selected.")
            else:
                success, message = register_user(email, password, role)
                if success:
                    st.success(message)
                else:
                    st.error(message)
