# app.py

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

# ✅ Page Setup
st.set_page_config(page_title="NextPlay NIL", layout="centered")

# ✅ Initialize State
st.session_state.setdefault("selected_sport", "Football")
is_admin = check_admin_access()
toggle_states = get_toggle_states()
partner_config = get_partner_config()
test_mode = st.sidebar.checkbox("🧪 Enable Test Mode", key="test_mode")

# ✅ Admin Tools
if is_admin:
    render_admin_banner()
    show_admin_dashboard()
    with st.sidebar:
        if st.button("🧩 Partner Config Panel", key="partner_panel_btn"):
            show_partner_admin()
            show_partner_toggle_panel()
    with st.sidebar.expander("📄 View Changelog", expanded=False):
        display_changelog()

# ✅ Partner Dashboard (only when both are true)
if is_admin and st.session_state.get("partner_mode", False):
    st.header("🧩 Partner Mode Dashboard")
    show_partner_toggle_panel()

# ✅ Show Ad (only when both toggles are on)
if toggle_states.get("enable_ads") and st.session_state.get("partner_toggle_enable_partner_ads"):
    st.markdown("### 📢 Sponsored Message")
    show_ad(location="header_ad", sport=st.session_state["selected_sport"])

# ✅ App Header
st.title("🏈 NextPlay NIL")
st.subheader("Own your brand. Win your next play.")
st.subheader("Your NIL Strategy & Branding Assistant")

# ✅ Step 0: NIL Course
with st.expander("🎓 NIL Education", expanded=False):
    run_nil_course()

# ✅ Step 1: NIL Readiness Quiz
def step_readiness_quiz():
    st.header("Step 1: NIL Readiness Quiz")
    quiz_score = 72 if test_mode else run_quiz()
    if quiz_score:
        st.success(f"🎯 Your NIL Match Score: {quiz_score}/100")
        st.markdown(calculate_score(quiz_score))
        earnings = earnings_estimator(quiz_score)
        st.info(f"💰 Estimated NIL Earning Potential: ${earnings:,.2f}")
    return quiz_score

if toggle_states.get("step_1", True):
    quiz_score = step_readiness_quiz()
else:
    quiz_score = None

# ✅ Step 2: Business Tool Generator
def step_business_tools():
    st.header("Step 2: NIL Business Tools")
    deal_type = st.selectbox("Pick your need:", ["Brand Outreach Email", "Contract Template", "Social Media Post", "Thank You Note"], key="deal_type_select")
    name = st.text_input("Enter Athlete or Brand Name", key="deal_name_input")
    if st.button("Generate My Template", key="generate_btn") and name:
        st.code(generate_template(deal_type, name), language="markdown")
    elif st.session_state.get("generate_btn") and not name:
        st.warning("Please enter a name or brand.")

if toggle_states.get("step_2", True):
    step_business_tools()

# ✅ Step 3: NIL Deal Builder
if toggle_states.get("step_3", True):
    st.header("🧾 Step 3: NIL Deal Builder Wizard")
    run_wizard()

# ✅ Step 4: Pitch Deck Generator
def step_pitch_deck():
    st.header("📊 Step 4: NIL Pitch Deck Generator")
    with st.form("pitch_form"):
        name = st.text_input("Your Name", key="pitch_name")
        sport = st.text_input("Sport", key="pitch_sport")
        followers = st.text_input("Social Followers", key="pitch_followers")
        stats = st.text_input("Top 3 Athletic Stats", key="pitch_stats")
        goals = st.text_area("What are your NIL goals?", key="pitch_goals")
        if st.form_submit_button("Generate Pitch Deck"):
            st.code(build_pitch_deck(name, sport, followers, stats, goals), language="markdown")

if toggle_states.get("step_4", True):
    step_pitch_deck()

# ✅ Step 5: Weekly Content Plan
if toggle_states.get("step_5", True):
    st.header("📅 Step 5: Weekly Content Plan")
    display_calendar()

# ✅ Step 6: NIL Success Stories
if toggle_states.get("step_6", True):
    st.header("📚 Step 6: Real NIL Success Stories")
    show_case_studies()

# ✅ Step 7: Contact Form
def step_contact_form(score):
    st.header("📥 Step 7: Stay in the NIL Loop")
    with st.form("contact_form"):
        name = st.text_input("Your Full Name", key="contact_name")
        email = st.text_input("Your Email", key="contact_email")
        school = st.text_input("School or Program", key="contact_school")
        submitted = st.form_submit_button("Submit")
    
    if submitted:
        if test_mode:
            pd.DataFrame([[name, email, school, score]], columns=["Name", "Email", "School", "Score"]).to_csv("test_mode_log.csv", mode="a", index=False, header=False)
            success = True
            email_body = get_email_body(name, score)
        else:
            record_to_sheet(name, email, school)
            success, email_body = send_email(name, email, score)
        
        if success:
            st.success("✅ Your info has been recorded. We will follow up with NIL tips and updates.")
            st.markdown("### 📄 Preview of Email Sent:")
            st.code(email_body)
            if st.button("📤 Resend Email", key="resend_email_btn"):
                send_email(name, email, score)

if toggle_states.get("step_7", True):
    step_contact_form(score=quiz_score or 0)

# ✅ Final Leaderboard
display_leaderboard()
