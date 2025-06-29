import streamlit as st
from utils.logger import log_change

# Central toggle label mapping for sidebar checkboxes
TOGGLE_KEYS = {
    "step_1": "Show Step 1: NIL Readiness Quiz",
    "step_2": "Show Step 2: NIL Business Tools",
    "step_3": "Show Step 3: Deal Builder Wizard",
    "step_4": "Show Step 4: Pitch Deck Generator",
    "step_5": "Show Step 5: Weekly Content Plan",
    "step_6": "Show Step 6: NIL Success Stories",
    "step_7": "Show Step 7: Contact Form & Updates",
    "show_pitch_deck": "Enable Pitch Deck Generator",
    "toggle_contract": "Show Contract Generator",
    "toggle_contact_form": "Lock Contact Form",
    "enable_ads": "Enable Ads"
}

# ✅ Now only reads the checkbox state instead of redrawing it
def check_admin_access():
    return st.session_state.get("admin_mode_checkbox", False)

def show_admin_dashboard():
    """Show toggles to manage visibility of app sections."""
    st.sidebar.subheader("🛠️ Admin Controls")
    for key, label in TOGGLE_KEYS.items():
        prev = st.session_state.get(key, True)
        new_val = st.sidebar.checkbox(label, value=prev, key=f"toggle_{key}")
        if new_val != prev:
            log_change(f"Toggled '{label}' from {prev} to {new_val}", actor="Admin")
        st.session_state[key] = new_val

def get_toggle_states():
    """Central access to current toggle states."""
    return {key: st.session_state.get(key, True) for key in TOGGLE_KEYS.keys()}

def render_admin_banner():
    st.markdown("🚨 **Admin Mode Active** — Use toggles to control app visibility.", unsafe_allow_html=True)
