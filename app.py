
import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import pytz

# Configuration
st.set_page_config(page_title="🏆 NIL Real-Time Dashboard", layout="wide")

# Timezone and time
tz = datetime.now().astimezone().tzinfo
current_time = datetime.now(tz).strftime("%A, %Y-%m-%d %I:%M %p %Z")
st.title("📊 NIL Agent Dashboard")
st.caption(f"🕒 Current time: {current_time}")

# Sidebar: Auth
st.sidebar.header("🔐 Login")
role = st.sidebar.selectbox("Select your role", ["athlete", "parent", "coach", "admin"])
user = st.sidebar.text_input("Enter your name or ID")
login = st.sidebar.button("Log in")

if login and user:
    st.session_state["role"] = role
    st.session_state["user"] = user
    st.session_state["session_id"] = f"{role}_{user}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

if "user" not in st.session_state:
    st.warning("Please log in from the sidebar.")
    st.stop()


# --- UI Toggles and Settings Panel ---
st.sidebar.markdown("## 🛠️ Dashboard Settings")

# --- Role-specific features ---
st.sidebar.subheader("🔐 Access Control")
lock_session = st.sidebar.checkbox("Lock Session (Disable Role Switching)", value=True)
admin_mode = st.sidebar.toggle("Admin Mode")

# --- AI Behavior Options ---
st.sidebar.subheader("🧠 AI Response Options")
coaching_tone = st.sidebar.toggle("Enable Coaching Tone", value=False)
classify_intent = st.sidebar.checkbox("Query Classification Mode", value=True)
summarize_response = st.sidebar.checkbox("Auto Summarize Response", value=True)

# --- Logging and History ---
st.sidebar.subheader("🗃 Logging & Export")
log_queries = st.sidebar.checkbox("Log All Queries", value=True)
local_only_log = st.sidebar.checkbox("Local Session Logging Only", value=False)
export_button = st.sidebar.button("📁 Export Filtered History to CSV")

supabase_sync = st.sidebar.toggle("Enable Supabase Sync", value=False)

# --- Chart Display Options ---
st.sidebar.subheader("📊 Analytics Controls")
show_charts = st.sidebar.toggle("Show Charts", value=True)
time_range = st.sidebar.selectbox("Time Range Filter", ["Today", "Last 7 Days", "Custom Range"])
search_scope = st.sidebar.radio("Search Scope", ["Query Only", "Response Only", "All Fields"])
group_by = st.sidebar.radio("Group Chart Data By", ["Role", "Category"])

# --- Personalization & UX ---
st.sidebar.subheader("🎨 Personalization")
dark_mode = st.sidebar.toggle("Dark Mode", value=False)
font_size = st.sidebar.slider("Font Size", 12, 24, 16)
typing_effect = st.sidebar.checkbox("Simulate AI Typing Effect", value=False)


# Google Sheets integration
def log_to_sheets(row):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            st.secrets["google"]["gcp_service_account"], scope
        )
        client = gspread.authorize(creds)
        sheet = client.open(st.secrets["google"]["sheet_name"]).sheet1
        sheet.append_row(row)
    except Exception as e:
        st.error(f"Logging failed: {e}")

# Chat input
st.subheader("💬 Ask Your NIL Question")
webhook_url = st.text_input("N8N Webhook URL", placeholder="https://your-n8n-server.com/webhook/nil-agent")
query = st.text_input("Ask a NIL-related question")

if webhook_url and query:
    with st.spinner("Consulting NIL Agent..."):
        try:
            response = requests.post(webhook_url, json={"query": query}, timeout=15)
            result = response.json()
            if result.get("success"):
                st.success("✅ Response")
                st.markdown(f"**Title:** {result.get('problem_title', 'N/A')}")
                st.markdown(f"**Description:** {result.get('problem_description', 'N/A')}")
                st.markdown(f"**Response:** {result.get('ai_response', 'No response available')}")
                # Log to Google Sheets
                log_to_sheets([
                    datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S"),
                    st.session_state["role"],
                    st.session_state["user"],
                    query,
                    result.get("ai_response", "N/A"),
                    st.session_state["session_id"]
                ])
            else:
                st.error(result.get("error", "Unknown error"))
        except Exception as e:
            st.error(f"Failed to connect: {e}")

# Chat History Viewer Tab
st.markdown("---")
st.subheader("📖 Chat History Viewer")
try:
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        st.secrets["google"]["gcp_service_account"], scope
    )
    client = gspread.authorize(creds)
    sheet = client.open(st.secrets["google"]["sheet_name"]).sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Filters
    st.markdown("### Filter Records")
    role_filter = st.selectbox("Filter by role", ["all"] + df["role"].unique().tolist())
    if role_filter != "all":
        df = df[df["role"] == role_filter]

    search_text = st.text_input("Search by keyword")
    if search_text:
        df = df[df["query"].str.contains(search_text, case=False, na=False)]

    st.dataframe(df.sort_values("timestamp", ascending=False))
except Exception as e:
    st.warning(f"Viewer failed to load: {e}")
