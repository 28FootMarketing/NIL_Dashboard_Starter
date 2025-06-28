# utils/admin_tools.py

import streamlit as st


TOGGLE_KEYS = {
    "step_1": "Show Step 1: NIL Readiness Quiz",
    "step_2": "Show Step 2: NIL Business Tools",
    "step_3": "Show Step 3: Deal Builder Wizard",
    "step_4": "Show Step 4: Pitch Deck Generator",
    "step_5": "Show Step 5: Weekly Content Plan",
    "step_6": "Show Step 6: NIL Success Stories",
    "step_7": "Show Step 7: Contact Form & Updates",
}

def check_admin_access():
    return st.sidebar.checkbox("👑 Admin Mode", key="admin_mode_checkbox")

def check_admin_access():
    # This should be replaced with actual login logic
    return st.sidebar.checkbox("👑 Admin Mode")

def show_admin_dashboard():
    st.sidebar.subheader("🛠️ Admin Controls")
    for key, label in TOGGLE_KEYS.items():
        if key not in st.session_state:
            st.session_state[key] = True
        st.session_state[key] = st.sidebar.checkbox(label, value=st.session_state[key])
