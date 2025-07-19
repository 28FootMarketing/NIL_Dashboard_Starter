
import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime
import pytz
from modules.NIL_Dashboard_Toggles_All import *
from modules.PDF_Export_Module import export_session_to_pdf
from modules.Knowledge_Center_Tab import show_knowledge_center
from modules.Team_Mode_Viewer import show_team_mode_view
from modules.Supabase_Logging_Block import log_to_supabase
# Theme Toggle
theme_mode = st.sidebar.radio("🌗 Theme Mode", ["Light", "Dark"], index=1)

# Apply Theme CSS
if theme_mode == "Dark":
    dark_css = '''
    <style>
        body {
            background-color: #0e1117;
            color: #cfcfcf;
        }
        .stApp {
            background-color: #0e1117;
            color: #cfcfcf;
        }
        .stTextInput>div>div>input, .stTextArea textarea {
            background-color: #1c1f26;
            color: #ffffff;
        }
        .css-1d391kg {
            background-color: #1c1f26 !important;
        }
    </style>
    '''
    st.markdown(dark_css, unsafe_allow_html=True)
else:
    st.markdown('<style>body{background-color:white;color:black;}</style>', unsafe_allow_html=True)

# Page Setup
st.set_page_config(page_title="🏆 NIL Real-Time Dashboard", layout="wide")
tz = datetime.now().astimezone().tzinfo
current_time = datetime.now(tz).strftime("%A, %Y-%m-%d %I:%M %p %Z")

st.title("📊 NIL Agent Dashboard (Theme Toggle Enabled)")
st.caption(f"🕒 Current time: {current_time}")
