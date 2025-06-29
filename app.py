# ✅ Load Global and Partner Toggles
toggle_states = get_toggle_states()
partner_config = get_partner_config()

# ✅ Sponsored Header Ad (Only if both global + partner toggles are on)
if toggle_states.get("enable_ads", False) and partner_config.get("partner_toggle_enable_partner_ads", False):
    st.markdown("### 📢 Sponsored Message")
    show_ad(location="header_ad", sport=st.session_state.get("selected_sport", "Football"))

# ✅ Step 0: NIL Education (Always Shown)
with st.expander("🎓 NIL Education"):
    run_nil_course()

# ✅ Step 1: NIL Readiness Quiz
if toggle_states.get("step_1", True) and not partner_config.get("partner_toggle_hide_quiz", False):
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
if toggle_states.get("step_4", True) and not partner_config.get("partner_toggle_hide_pitch_deck", False):
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
if toggle_states.get("step_6", True) and partner_config.get("partner_toggle_enable_testimonials", True):
    st.header("📚 Step 6: Real NIL Success Stories")
    show_case_studies()

# ✅ Step 7: Contact Form
if toggle_states.get("step_7", True) and not partner_config.get("partner_toggle_hide_contact_form", False):
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

# ✅ Always Show Leaderboard
display_leaderboard()
