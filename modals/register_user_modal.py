import streamlit as st
from auth.auth_logic import register_user

def register_user_modal():
    with st.expander("🆕 Create New Account", expanded=False):
        st.markdown("Register a new user below.")

        email = st.text_input("Email", key="register_email_modal")
        password = st.text_input("Password", type="password", key="register_password_modal")
        role = st.selectbox("Role", ["user", "admin"], key="register_role_modal")

        if st.button("Register Now", key="register_button_modal"):
            result = register_user(email, password, role)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["error"])
