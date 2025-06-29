import streamlit as st

# Centralized keys for partner-specific visibility toggles
PARTNER_TOGGLE_KEYS = {
    "partner_toggle_enable_partner_ads": "Partner: Enable Ads",
    "partner_toggle_hide_quiz": "Partner: Hide NIL Readiness Quiz",
    "partner_toggle_hide_pitch_deck": "Partner: Hide Pitch Deck Generator",
    "partner_toggle_hide_contact_form": "Partner: Hide Contact Form",
    "partner_toggle_enable_testimonials": "Partner: Enable NIL Testimonials",
    "partner_toggle_allow_custom_offers": "Partner: Allow Custom NIL Offer Uploads"
}

def get_partner_config():
    """Returns the current state of each partner toggle."""
    return {key: st.session_state.get(key, True) for key in PARTNER_TOGGLE_KEYS.keys()}

def show_partner_toggle_panel():
    """Display partner-specific visibility controls in the sidebar."""
    st.subheader("🎛️ Partner Visibility Toggles")
    for key, label in PARTNER_TOGGLE_KEYS.items():
        previous = st.session_state.get(key, True)
        new_value = st.checkbox(label, value=previous, key=key)
        if new_value != previous:
            st.session_state[key] = new_value
