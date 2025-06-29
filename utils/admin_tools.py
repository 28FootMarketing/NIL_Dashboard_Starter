import streamlit as st
from utils.logger import log_change
from utils.persistent_toggle_store import load_toggles, save_toggles

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
    "enable_ads": "Enable Ads",
}

def check_admin_access():
   """Ensure Admin Mode toggle is only created once."""
    if "admin_mode_checkbox" not in st.session_state:
        st.session_state.admin_mode_checkbox = st.sidebar.checkbox("👑 Admin Mode")
    return st.session_state.admin_mode_checkbox

def show_admin_dashboard():
    """Show toggles to manage visibility of app sections."""
    st.sidebar.subheader("🛠️ Admin Controls")
    toggles = load_toggles()

    for key, label in TOGGLE_KEYS.items():
        prev = toggles.get(key, True)
        new_val = st.sidebar.checkbox(label, value=prev)
        if new_val != prev:
            log_change(f"Toggled '{label}' from {prev} to {new_val}", actor="Admin")
        st.session_state[key] = new_val
        toggles[key] = new_val

    save_toggles(toggles)
def get_toggle_states():
    """Central access to current toggle states."""
    return {key: st.session_state.get(key, True) for key in TOGGLE_KEYS.keys()}

def render_admin_banner():
    """Visual indicator that admin mode is active."""
    st.markdown("🚨 **Admin Mode Active** — Use toggles to control app visibility.", unsafe_allow_html=True)
