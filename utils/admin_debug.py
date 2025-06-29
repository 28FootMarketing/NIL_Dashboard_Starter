import streamlit as st
from utils.contact_handler import send_email
from utils.leaderboard import earnings_estimator

def render_admin_debug_panel():
    st.markdown("## 📊 Admin Analytics Panel")
    
    st.markdown("**Session Metrics**")
    active_users = 14  # TODO: Replace with dynamic value from DB or tracking system
    errors_today = 2   # TODO: Hook into logging system
    
    quiz_score = st.session_state.get("last_quiz_score", 0)
    earnings = earnings_estimator(quiz_score)

    st.write("👥 Active Users:", active_users)
    st.write("🚨 Errors Logged Today:", errors_today)
    st.write("📈 Last Quiz Score:", quiz_score)
    st.write("💰 Earnings Estimate:", f"${earnings:,.2f}")

    st.markdown("---")
    st.markdown("**Debug Tools**")

    if st.button("📤 Force Email Test"):
        send_email("Test Admin", "admin@example.com", 88)
        st.success("✅ Test email sent.")

    if st.button("♻️ Reset App State"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
