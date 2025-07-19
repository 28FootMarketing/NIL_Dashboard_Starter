from auth.auth_logic import login, is_logged_in, get_user_role
from panels.admin_panel import show_admin_panel
from modules.NIL_Dashboard_Toggles_All import show_dashboard

if not is_logged_in():
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(email, password)
        st.rerun()
else:
    user_role = get_user_role(st.session_state.user.email)
    st.sidebar.success(f"Logged in as {user_role}")

    if user_role == "coach":
        show_admin_panel()
    else:
        show_dashboard()
