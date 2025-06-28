# utils/changelog_viewer.py

import streamlit as st

def display_changelog():
    try:
        with open("changelog.txt", "r") as file:
            changelog = file.read()
            st.markdown("## 📝 Changelog")
            st.code(changelog, language="text")
    except FileNotFoundError:
        st.warning("Changelog file not found.")
