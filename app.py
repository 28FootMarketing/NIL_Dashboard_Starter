# app.py

import streamlit as st
import pandas as pd

# ✅ Utility Imports
from utils.quiz_logic import run_quiz
from utils.content_templates import generate_template
from utils.nil_score import calculate_score
from utils.leaderboard import display_leaderboard, earnings_estimator
from utils.pitch_deck_generator import build_pitch_deck
from utils.calendar_generator import display_calendar
from utils.nil_wizard import run_wizard
from utils.case_studies import show_case_studies
from utils.course_quiz import run_nil_course
from utils.contact_handler import record_to_sheet, send_email, get_email_body
from utils.admin_tools import check_admin_access, show_admin_dashboard, get_toggle_states, render_admin_banner
from utils.partner_admin import show_partner_admin
from utils.advertisements import show_ad
from utils.partner_config import PartnerConfigHelper
from utils.changelog_viewer import display_changelog
from utils.partner_dashboard import PartnerDashboard

# ✅ Page Setup
st.set_page_config(page_title="NextPlay NIL", layout="centered")

# ✅ Session State Initialization
if "selected_sport" not in st.session_state:
    st.session_state["selected_sport"] = "Football"

# ✅ Partner Config Defaults
PartnerConfigHelper.initialize_defaults()

# ✅ Admin Mode
# ✅ Admin + Partner Tier Access Check
partner_config = PartnerConfigHelper.get_config()
is_admin = check_admin_access()
has_admin_access = is_admin and partner_config.get("partner_tier") == "Gold"

if has_admin_access:
    render_admin_banner()
    show_admin_dashboard()

    with st.sidebar:
        st.markdown("## 🧩 White-Label Settings")

        # Toggle Partner Mode
        partner_mode = st.session_state.get("partner_mode", False)
        if st.button("✅ Enable Partner Mode" if not partner_mode else "❌ Disable Partner Mode"):
            st.session_state["partner_mode"] = not partner_mode
            st.experimental_rerun()

        # Show Partner Config Panel if enabled
        if st.session_state.get("partner_mode", False):
            config_panel_open = st.session_state.get("show_partner_config_panel", False)
            if st.button("⚙️ " + ("Close" if config_panel_open else "Open") + " Config Panel"):
                st.session_state["show_partner_config_panel"] = not config_panel_open
                st.experimental_rerun()

            with st.expander("🧱 Config Panel"):
                show_partner_admin()

        st.markdown("### 📄 Changelog")
        display_changelog()


            with st.expander("🧱 Config Panel"):
                show_partner_admin()

        st.markdown("### 📄 Changelog")
        display_changelog()
   
col1, col2 = st.columns(2)
if col1.button("✏️ Edit Partner"):
    st.success("Ready to edit. Make your changes below.")

if col2.button("🗑️ Delete Partner"):
    del configs[selected]
    PartnerConfigHelper.save_config(selected=None, config_data=configs)
    st.warning(f"Partner '{selected}' deleted. Refresh the page.")
    st.stop()
    
    render_admin_sidebar()

# ✅ Test Mode
with st.sidebar:
    test_mode = st.checkbox("🧪 Enable Test Mode (Safe Demo)")
    if test_mode:
        st.warning("Test Mode is ON — No data will be saved or emailed.")
        st.markdown("### ⚠️ TEST MODE: No data will be sent or stored.", unsafe_allow_html=True)

# ✅ Load Feature Toggles
toggle_states = get_toggle_states()

# ✅ Sponsored Header Ad
partner_config = PartnerConfigHelper.get_config()
if toggle_states.get("enable_ads", False) and partner_config.get("enable_partner_ads", False):
    st.markdown("### 📢 Sponsored Message")
    show_ad(location="header_ad", sport=st.session_state.get("selected_sport", "Football"))

# ✅ App Title
st.title("🏈 NextPlay NIL")
st.subheader("Own your brand. Win your next play.")
st.subheader("Your NIL Strategy & Branding Assistant")

# 🎓 Step 0: Education
with st.expander("🎓 NIL Education"):
    run_nil_course()

# ✅ Step 1: NIL Readiness Quiz
if toggle_states.get("step_1", True):
    st.header("Step 1: NIL Readiness Quiz")
    quiz_score = 72 if test_mode else run_quiz()
    if quiz_score:
        st.success(f"🎯 Your NIL Match Score: {quiz_score}/100")
        st.markdown(calculate_score(quiz_score))
        estimated_earnings = earnings_estimator(quiz_score)
        st.info(f"💰 Estimated NIL Earning Potential: ${estimated_earnings:,.2f}")

# ✅ Step 2: NIL Business Tools
if toggle_states.get("step_2", True):
    st.header("Step 2: NIL Business Tools")
    deal_type = st.selectbox("Pick your need:", ["Brand Outreach Email", "Contract Template", "Social Media Post", "Thank You Note"])
    custom_name = st.text_input("Enter Athlete or Brand Name:")
    if st.button("Generate My Template"):
        if custom_name:
            st.code(generate_template(deal_type, custom_name), language='markdown')
        else:
            st.warning("Please enter a name or brand.")

# ✅ Step 3: Deal Builder Wizard
if toggle_states.get("step_3", True):
    st.header("🗾 Step 3: NIL Deal Builder Wizard")
    run_wizard()

# ✅ Step 4: Pitch Deck Generator
if toggle_states.get("step_4", True):
    st.header("📊 Step 4: NIL Pitch Deck Generator")
    with st.form("pitch_deck_form"):
        name = st.text_input("Your Name")
        sport = st.text_input("Sport")
        followers = st.text_input("Social Followers (e.g., 2500 IG, 1200 TikTok)")
        stats = st.text_input("Top 3 Athletic Stats")
        goals = st.text_area("What are your NIL goals?")
        pitch_submitted = st.form_submit_button("Generate Pitch Deck")
        if pitch_submitted:
            st.code(build_pitch_deck(name, sport, followers, stats, goals), language='markdown')

# ✅ Step 5: Weekly Content Plan
if toggle_states.get("step_5", True):
    st.header("📅 Step 5: Weekly Content Plan")
    display_calendar()

# ✅ Step 6: NIL Success Stories
if toggle_states.get("step_6", True):
    st.header("📚 Step 6: Real NIL Success Stories")
    show_case_studies()

# ✅ Step 7: Contact Form
if toggle_states.get("step_7", True):
    st.header("📥 Step 7: Stay in the NIL Loop")
    with st.form("contact_form"):
        name = st.text_input("Your Full Name")
        email = st.text_input("Your Email")
        school = st.text_input("School or Program")
        submitted = st.form_submit_button("Submit")

    if submitted:
        try:
            if not test_mode:
                record_to_sheet(name, email, school)
                success, email_body = send_email(name, email, quiz_score)
            else:
                pd.DataFrame([[name, email, school, quiz_score]], columns=["Name", "Email", "School", "Score"]) \
                    .to_csv("test_mode_log.csv", mode="a", index=False, header=False)
                success = True
                email_body = get_email_body(name, quiz_score)

            if success:
                st.success("✅ Your info has been recorded. We will follow up with NIL tips and updates.")
                st.markdown("### 📄 Preview of Email Sent:")
                st.code(email_body)
                if st.button("📤 Resend Email"):
                    send_email(name, email, quiz_score)

        except Exception as e:
            st.error(f"An error occurred while submitting your form: {e}")

# ✅ Leaderboard
display_leaderboard()
