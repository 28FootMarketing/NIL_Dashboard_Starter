# --- 1. Imports ---
import streamlit as st
from modules.NIL_Dashboard_Toggles_All import show_dashboard
from modules.admin_dashboard import admin_dashboard
from auth.auth_logic import login, is_logged_in, get_user_role, reset_password
from toggles.toggle_flags import load_toggle_flags
from modals.register_user_modal import register_user_modal

# --- 2. Session Setup ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "user_email" not in st.session_state:
    st.session_state["user_email"] = ""
if "user_role" not in st.session_state:
    st.session_state["user_role"] = ""

def logout():
    st.session_state["authenticated"] = False
    st.session_state["user_email"] = ""
    st.session_state["user_role"] = ""
    st.experimental_rerun()

# --- 3. Main App Logic ---
def main():
    st.set_page_config(page_title="🏆 NIL Agent Dashboard", layout="wide")

    if not st.session_state["authenticated"]:
        st.title("🔐 NIL Dashboard Login")

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if not email or not password:
                st.error("Email and password are required.")
            elif login(email, password):
                st.session_state["authenticated"] = True
                st.session_state["user_email"] = email
                st.session_state["user_role"] = get_user_role(email)
                st.success(f"✅ Login successful as {st.session_state['user_role']}")
                st.experimental_rerun()
            else:
                st.error("❌ Invalid email or password")

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
    else:
        st.title("🏆 NIL Agent Dashboard")
        st.success(f"Logged in as {st.session_state['user_email']} ({st.session_state['user_role']})")
        st.button("Logout", on_click=logout)

        # --- Role Routing ---
        if st.session_state["user_role"] == "admin":
            admin_dashboard(user_email=st.session_state["user_email"])
        elif st.session_state["user_role"] in ["coach", "athlete"]:
            show_dashboard(user_role=st.session_state["user_role"])
        else:
            st.warning("Access denied. Role not recognized.")
            logout()

# --- 4. Launch ---
if __name__ == "__main__":
    main()
