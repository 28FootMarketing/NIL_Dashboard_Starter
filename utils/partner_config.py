# ✅ partner_config.py

def get_partner_config():
    # Placeholder for now, should later load from DB or secure config file
    return {
        "partner_toggle_hide_quiz": False,
        "partner_toggle_hide_tools": False,
        "partner_toggle_hide_wizard": False,
        "partner_toggle_hide_pitchdeck": False,
        "partner_toggle_hide_calendar": False,
        "partner_toggle_hide_stories": False,
        "partner_toggle_hide_contact_form": False,
        "partner_toggle_enable_partner_ads": True
    }

def show_partner_toggle_panel():
    import streamlit as st
    st.markdown("### 🧩 Partner Visibility Toggles")

    for key, label in [
        ("partner_toggle_hide_quiz", "Hide Step 1: NIL Readiness Quiz"),
        ("partner_toggle_hide_tools", "Hide Step 2: NIL Business Tools"),
        ("partner_toggle_hide_wizard", "Hide Step 3: Deal Builder Wizard"),
        ("partner_toggle_hide_pitchdeck", "Hide Step 4: Pitch Deck Generator"),
        ("partner_toggle_hide_calendar", "Hide Step 5: Weekly Content Plan"),
        ("partner_toggle_hide_stories", "Hide Step 6: NIL Success Stories"),
        ("partner_toggle_hide_contact_form", "Hide Step 7: Contact Form"),
        ("partner_toggle_enable_partner_ads", "Enable Partner Ads")
    ]:
        current_val = st.session_state.get(key, False)
        new_val = st.checkbox(label, value=current_val, key=f"{key}_panel")
        st.session_state[key] = new_val
