import streamlit as st
import pandas as pd

# Utility Imports
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
from utils.partner_config import get_partner_config, show_partner_toggle_panel
from utils.changelog_viewer import display_changelog
from utils.partner_banner_editor import show_partner_banner_editor
from utils.logger import log_change
from utils.partner_branding import show_brand_preview_panel
from utils.partner_resources import show_partner_resources

# ✅ Page Setup
st.set_page_config(page_title="NextPlay NIL", layout="centered")

# ✅ Session State Initialization
if "selected_sport" not in st.session_state:
    st.session_state["selected_sport"] = "Football"

# ✅ Admin Mode
is_admin = check_admin_access()
if is_admin:
    render_admin_banner()
    show_admin_dashboard()

    with st.sidebar:
        if st.button("🧩 Partner Config Panel"):
            show_partner_admin()
            show_partner_toggle_panel()

        if st.button("📝 Edit Partner Message"):
            st.session_state["show_banner_editor"] = True

    with st.sidebar.expander("📄 View Changelog"):
        display_changelog()

    if st.session_state.get("show_banner_editor", False):
        st.subheader("📝 Partner Message Editor")
        show_partner_banner_editor()
if is_admin and st.session_state.get("partner_mode", True):
    st.markdown("## 🧩 Partner Branding Settings")
    show_brand_preview_panel(partner_config)

# ✅ Partner Mode Dashboard (Admin only)
if is_admin and st.session_state.get("partner_mode", True):
    st.header("🧩 Partner Mode Dashboard")
    show_partner_toggle_panel()
    # display_partner_leads()  # Uncomment when implemented

# ✅ Test Mode
test_mode = st.sidebar.checkbox("🧪 Enable Test Mode (Safe Demo)")
if test_mode:
    st.sidebar.warning("Test Mode is ON — No data will be saved or emailed.")
    st.markdown("### ⚠️ TEST MODE: No data will be sent or stored.", unsafe_allow_html=True)

# ✅ Load Feature Toggles
toggle_states = get_toggle_states()

# ✅ Sponsored Header Ad (Only if both global + partner toggles are on)
partner_config = get_partner_config()
if (
    toggle_states.get("enable_ads", False)
    and st.session_state.get("partner_toggle_enable_partner_ads", False)
    and partner_config.get("show_partner_banner", True)
):
    st.markdown("### 📢 Sponsored Message")
    st.info(partner_config.get("partner_banner_message", "Partner promotion message coming soon."))

# ✅ App Branding
st.title("🏈 NextPlay NIL")
st.subheader("Own your brand. Win your next play.")
st.subheader("Your NIL Strategy & Branding Assistant")

# ✅ RESOURCES
if partner_config.get("partner_toggle_show_resources", False):
    st.header("📚 Partner Resource Library")
    show_partner_resources(partner_config.get("partner_id", "default"))
    
# ✅ Step 0: NIL Education (Always Shown)
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
            st.code(generate_template(deal_type, custom_name), language="markdown")
        else:
            st.warning("Please enter a name or brand.")

# ✅ Step 3: Deal Builder Wizard
if toggle_states.get("step_3", True):
    st.header("🧾 Step 3: NIL Deal Builder Wizard")
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
            st.code(build_pitch_deck(name, sport, followers, stats, goals), language="markdown")

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

display_leaderboard(school=school_filter, sport=sport_filter, partner=partner_filter)

# ✅ Always Show Leaderboard
display_leaderboard()
school_filter = st.sidebar.selectbox("Filter by School", ["All"] + school_list)
sport_filter = st.sidebar.selectbox("Filter by Sport", ["All"] + sport_list)
partner_filter = st.sidebar.selectbox("Filter by Partner", ["All"] + partner_list)
