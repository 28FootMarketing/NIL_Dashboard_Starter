# nil_wizard.py
import streamlit as st

def run_wizard():
    st.write("🛠️ Build a mock NIL offer now:")
    brand = st.text_input("Brand Name")
    offer_type = st.selectbox("Type of NIL Opportunity", [
        "Post on IG", 
        "Wear gear", 
        "Make a video", 
        "Host a giveaway", 
        "Attend an event", 
        "Create a shoutout video", 
        "Use a product in content", 
        "Join a podcast", 
        "Write a blog or caption",
        "Other"
    ])
    payment = st.text_input("Proposed Payment Amount ($)")
    deadline = st.date_input("Delivery Deadline")

    if st.button("Build Offer"):
        st.markdown(f"**NIL Opportunity Summary**\n\nBrand: {brand}\nType: {offer_type}\nPayment: ${payment}\nDue: {deadline}")
