# nil_wizard.py
import streamlit as st

def run_wizard():
    st.write("🛠️ Build Your NIL Deal Offer")

    brand = st.text_input("Brand Name")

    # Select multiple platforms
    platforms = st.multiselect(
        "Which platforms will this NIL opportunity use?",
        ["Instagram", "TikTok", "YouTube", "Twitter", "Snapchat", "Podcast", "Blog", "In-person Event", "Other"]
    )

    offer_type = st.selectbox("Type of NIL Opportunity", [
        "Post on Social Media", 
        "Wear or Use a Product", 
        "Attend a Brand Event", 
        "Create Sponsored Video", 
        "Host a Giveaway", 
        "Write Sponsored Caption or Blog", 
        "Join an Interview or Podcast", 
        "Other"
    ])

    payment = st.text_input("Proposed Payment Amount ($)")
    deadline = st.date_input("Delivery Deadline")
    notes = st.text_area("Additional Deal Notes (optional)")

    if st.button("Build Offer Summary"):
        st.markdown("### 📄 NIL Opportunity Summary")
        st.markdown(f"**Brand:** {brand}")
        st.markdown(f"**Deal Type:** {offer_type}")
        if platforms:
            st.markdown("**Platforms:** " + ", ".join(platforms))
        st.markdown(f"**Payment:** ${payment}")
        st.markdown(f"**Deadline:** {deadline}")
        if notes:
            st.markdown(f"**Notes:** {notes}")
