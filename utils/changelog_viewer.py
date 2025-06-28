# utils/changelog_viewer.py

import streamlit as st
from fpdf import FPDF
import os

def display_changelog():
    try:
        with open("changelog.txt", "r") as file:
            changelog = file.read()
            st.markdown("## 📝 Changelog")
            st.code(changelog, language="text")

            if st.button("⬇️ Download PDF Version"):
                pdf_path = generate_changelog_pdf(changelog)
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="📥 Save Changelog as PDF",
                        data=f,
                        file_name="changelog.pdf",
                        mime="application/pdf"
                    )
    except FileNotFoundError:
        st.warning("Changelog file not found.")

def generate_changelog_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=10)

    for line in text.splitlines():
        pdf.cell(0, 6, line, ln=True)

    output_path = "generated_changelog.pdf"
    pdf.output(output_path)
    return output_path
