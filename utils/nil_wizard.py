# nil_wizard.py
import streamlit as st
import os
from fpdf import FPDF
import datetime

def run_wizard():
    st.write("🛠️ Build Your NIL Deal Offer")

    brand = st.text_input("Brand Name")

    platforms = st.multiselect(
        "Which platforms will this NIL opportunity use?",
        ["Instagram", "TikTok", "YouTube", "X", "Snapchat", "LinkedIn", "Facebook", "Podcast", "Blog", "In-person Event", "Other"]
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

    athlete_name = st.text_input("Athlete Full Name")
    email = st.text_input("Your Email (to receive contract PDF)")

    def generate_pdf(athlete, brand, offer_type, platforms, payment, deadline, notes):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="NIL Agreement Summary", ln=True, align='C')
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"""
Athlete: {athlete}
Brand: {brand}
Deal Type: {offer_type}
Platforms: {', '.join(platforms)}
Payment: ${payment}
Deadline: {deadline}
Notes: {notes}
    """.strip())
    
    pdf.ln(10)
    pdf.set_font("Arial", "I", 9)
    pdf.multi_cell(0, 8, txt="Disclaimer: This document is a self-generated NIL proposal. It is not a legally binding contract. All agreements must be reviewed and approved by your school, guardian, or legal advisor before execution.")
        
   # ✅ Ensure directory exists
    output_dir = "/mnt/data"
    os.makedirs(output_dir, exist_ok=True)

    filename = f"contract_{athlete.replace(' ', '_')}_{datetime.date.today()}.pdf"
    filepath = os.path.join(output_dir, filename)

    try:
        pdf.output(filepath)
        return filepath
    except Exception as e:
        st.error(f"❌ PDF generation failed: {e}")
        return None
    if st.button("Build Offer Summary"):
        st.markdown("### 📄 NIL Opportunity Summary")
        st.markdown(f"**Athlete:** {athlete_name}")
        st.markdown(f"**Brand:** {brand}")
        st.markdown(f"**Deal Type:** {offer_type}")
        if platforms:
            st.markdown("**Platforms:** " + ", ".join(platforms))
        st.markdown(f"**Payment:** ${payment}")
        st.markdown(f"**Deadline:** {deadline}")
        if notes:
            st.markdown(f"**Notes:** {notes}")

        if athlete_name and brand and offer_type:
            pdf_path = generate_pdf(athlete_name, brand, offer_type, platforms, payment, deadline, notes)
           if pdf_path:
    st.success("✅ Contract PDF Generated!")
    st.markdown(f"[📄 Download Contract PDF]({pdf_path})")
    if email:
        st.info(f"To email this file manually, attach the PDF located here: `{pdf_path}` and send to: {email}")
else:
    st.error("PDF generation failed.")

            if email:
                st.info(f"To email this file manually, attach the PDF located here: `{pdf_path}` and send to: {email}")
