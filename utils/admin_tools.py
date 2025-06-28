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
def get_toggle_states():
    return {
        "show_pitch_deck": st.session_state.get("show_pitch_deck", True),
        "show_contract_generator": st.session_state.get("toggle_contract", True),
        "lock_contact_form": st.session_state.get("toggle_contact_form", False),
        "enable_ads": st.session_state.get("enable_ads", False),
        # Add more as needed
    }

def get_toggle_states():
    """Returns the current toggle states for each step."""
    return {
        "step_1": st.session_state.get("step_1", True),
        "step_2": st.session_state.get("step_2", True),
        "step_3": st.session_state.get("step_3", True),
        "step_4": st.session_state.get("step_4", True),
        "step_5": st.session_state.get("step_5", True),
        "step_6": st.session_state.get("step_6", True),
        "step_7": st.session_state.get("step_7", True),
    }

def render_admin_banner():
    st.markdown("🚨 **Admin Mode Active** — Use toggles to control app visibility.", unsafe_allow_html=True)

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
    st.sidebar.checkbox("Enable Ads", key="enable_ads")
