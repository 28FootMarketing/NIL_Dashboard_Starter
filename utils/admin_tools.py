import streamlit as st
from utils.logger import log_change

# Unique keys for admin toggles
TOGGLE_KEYS = {
    "admin_toggle_step_1": "Show Step 1: NIL Readiness Quiz",
    "admin_toggle_step_2": "Show Step 2: NIL Business Tools",
    "admin_toggle_step_3": "Show Step 3: Deal Builder Wizard",
    "admin_toggle_step_4": "Show Step 4: Pitch Deck Generator",
    "admin_toggle_step_5": "Show Step 5: Weekly Content Plan",
    "admin_toggle_step_6": "Show Step 6: NIL Success Stories",
    "admin_toggle_step_7": "Show Step 7: Contact Form & Updates",
    "admin_toggle_show_pitch_deck": "Enable Pitch Deck Generator",
    "admin_toggle_contract": "Show Contract Generator",
    "admin_toggle_contact_form": "Lock Contact Form",
    "admin_toggle_enable_ads": "Enable Ads"
}

def check_admin_access():
    return st.sidebar.checkbox("👑 Admin Mode", key="admin_mode_checkbox")

def show_admin_dashboard():
    st.sidebar.subheader("🛠️ Admin Controls")
    for key, label in TOGGLE_KEYS.items():
        prev = st.session_state.get(key, True)
        new_val = st.sidebar.checkbox(label, value=prev, key=f"admin_dashboard_{key}")
        if new_val != prev:
            log_change(f"Toggled '{label}' from {prev} to {new_val}", actor="Admin")
        st.session_state[key] = new_val

def get_toggle_states():
    return {key: st.session_state.get(key, True) for key in TOGGLE_KEYS.keys()}

def render_admin_banner():
    st.markdown("🚨 **Admin Mode Active** — Use toggles to control app visibility.", unsafe_allow_html=True)
