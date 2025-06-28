import streamlit as st
import pandas as pd
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
from utils.admin_tools import check_admin_access, show_admin_dashboard

st.set_page_config(page_title="NextPlay NIL", layout="centered")
test_mode = st.sidebar.checkbox("🧪 Enable Test Mode (Safe Demo)")

if test_mode:
    st.sidebar.warning("Test Mode is ON — No data will be saved or emailed.")
    st.markdown('### ⚠️ TEST MODE: This is a safe demo version. No data will be sent or stored online.', unsafe_allow_html=True)

st.set_page_config(page_title="NextPlay NIL", layout="centered")
st.title("🏈 NextPlay NIL")
st.subheader("Own your brand. Win your next play.")
st.subheader("Your NIL Strategy & Branding Assistant")

with st.expander("🎓 NIL Education"):
    run_nil_course()

st.header("Step 1: NIL Readiness Quiz")
quiz_score = 72 if test_mode else run_quiz()

if quiz_score:
    st.success(f"🎯 Your NIL Match Score: {quiz_score}/100")
    st.markdown(calculate_score(quiz_score))
    estimated_earnings = earnings_estimator(quiz_score)
    st.info(f"💰 Estimated NIL Earning Potential: ${estimated_earnings:,.2f}")

st.header("Step 2: NIL Business Tools")
deal_type = st.selectbox("Pick your need:", ["Brand Outreach Email", "Contract Template", "Social Media Post", "Thank You Note"])
custom_name = st.text_input("Enter Athlete or Brand Name:")
if st.button("Generate My Template"):
    if custom_name:
        st.code(generate_template(deal_type, custom_name), language='markdown')
    else:
        st.warning("Please enter a name or brand.")

st.header("🧾 Step 3: NIL Deal Builder Wizard")
run_wizard()

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

st.header("📅 Step 5: Weekly Content Plan")
display_calendar()

st.header("📚 Step 6: Real NIL Success Stories")
show_case_studies()

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
        pd.DataFrame([[name, email, school, quiz_score]], columns=['Name', 'Email', 'School', 'Score'])             .to_csv('test_mode_log.csv', mode='a', index=False, header=False)
        success = True
        email_body = get_email_body(name, quiz_score)

    if success:
        st.success("✅ Your info has been recorded. We will follow up with NIL tips and updates.")
        st.markdown('### 📄 Preview of Email Sent:')
        st.code(email_body)
        if st.button('📤 Resend Email'):
            send_email(name, email, quiz_score)

display_leaderboard()
if is_admin:
    show_admin_dashboard()
