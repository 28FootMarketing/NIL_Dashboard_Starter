
import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime
import pytz

st.set_page_config(
    page_title="🏆 NIL Real-Time Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Get user timezone using streamlit runtime
tz = datetime.now().astimezone().tzinfo
current_time = datetime.now(tz).strftime("%A, %Y-%m-%d %I:%M %p %Z")

st.title("📊 NIL Agent Real-Time Dashboard")
st.caption(f"🕒 Current time: {current_time}")

st.markdown("#### Live Interaction Dashboard (connected to your NIL Agent on n8n)")

# Webhook settings
webhook_url = st.sidebar.text_input(
    "N8N Webhook URL",
    placeholder="https://your-n8n-server.com/webhook/nil-agent",
    help="Ensure your n8n workflow returns structured JSON."
)

# Example query for live response
sample_query = st.text_input("Ask a NIL-related question:")

if sample_query and webhook_url:
    with st.spinner("Querying NIL Agent..."):
        try:
            response = requests.post(webhook_url, json={"query": sample_query}, timeout=15)
            result = response.json()
            if result.get("success"):
                st.success("✅ AI Response")
                st.markdown(f"**Title:** {result.get('problem_title', 'N/A')}")
                st.markdown(f"**Description:** {result.get('problem_description', 'N/A')}")
                st.markdown(f"**Response:** {result.get('ai_response', 'No response available')}")
            else:
                st.error(f"Error: {result.get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"⚠️ Failed to fetch from NIL Agent: {e}")

# Historical Data Simulation for Charts
mock_data = pd.DataFrame([
    {"timestamp": "2025-07-01 14:32", "user": "Maliyah", "role": "Athlete", "query": "Can I sell my jersey?", "category": "Merchandise"},
    {"timestamp": "2025-07-01 14:35", "user": "Coach Carter", "role": "Coach", "query": "How do NIL rules affect scholarships?", "category": "Scholarship"},
    {"timestamp": "2025-07-02 09:12", "user": "Derek", "role": "Parent", "query": "Can boosters offer deals?", "category": "Compliance"},
    {"timestamp": "2025-07-02 10:45", "user": "Tamia", "role": "Athlete", "query": "What is NIL exactly?", "category": "Basics"},
    {"timestamp": "2025-07-03 13:01", "user": "Maliyah", "role": "Athlete", "query": "Can I promote energy drinks?", "category": "Brand"},
])

st.markdown("---")
st.subheader("📈 Mock Query Data Insights")
col1, col2, col3 = st.columns(3)
col1.metric("Total Queries", len(mock_data))
col2.metric("Unique Users", mock_data['user'].nunique())
col3.metric("Top Category", mock_data['category'].value_counts().idxmax())

st.dataframe(mock_data)

# Charts
st.subheader("🧠 Top NIL Question Categories")
fig1 = px.bar(mock_data['category'].value_counts().reset_index(), x='index', y='category',
              labels={'index': 'Category', 'category': 'Count'}, color='index')
st.plotly_chart(fig1, use_container_width=True)

st.subheader("👥 User Role Distribution")
fig2 = px.pie(mock_data, names='role', title='Distribution by User Role')
st.plotly_chart(fig2, use_container_width=True)
