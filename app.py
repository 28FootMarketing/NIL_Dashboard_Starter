
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="🏆 NIL Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sample mock data
data = pd.DataFrame([
    {"timestamp": "2025-07-01 14:32", "user": "Maliyah", "role": "Athlete", "query": "Can I sell my jersey?", "category": "Merchandise"},
    {"timestamp": "2025-07-01 14:35", "user": "Coach Carter", "role": "Coach", "query": "How do NIL rules affect scholarships?", "category": "Scholarship"},
    {"timestamp": "2025-07-02 09:12", "user": "Derek", "role": "Parent", "query": "Can boosters offer deals?", "category": "Compliance"},
    {"timestamp": "2025-07-02 10:45", "user": "Tamia", "role": "Athlete", "query": "What is NIL exactly?", "category": "Basics"},
    {"timestamp": "2025-07-03 13:01", "user": "Maliyah", "role": "Athlete", "query": "Can I promote energy drinks?", "category": "Brand"},
])

st.title("📊 NIL Agent Analytics Dashboard")

# KPIs
st.subheader("📈 Key Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Total Queries", len(data))
col2.metric("Unique Users", data['user'].nunique())
col3.metric("Last Query Time", data['timestamp'].max())

# Query Log
st.subheader("📋 Query Log")
st.dataframe(data)

# Most Asked Categories
st.subheader("🧠 Most Asked NIL Categories")
category_counts = data['category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Count']
fig = px.bar(category_counts, x='Category', y='Count', color='Category', title="Most Asked Topics")
st.plotly_chart(fig, use_container_width=True)

# Role Distribution
st.subheader("👥 User Role Distribution")
role_counts = data['role'].value_counts().reset_index()
role_counts.columns = ['Role', 'Count']
fig2 = px.pie(role_counts, values='Count', names='Role', title="Users by Role")
st.plotly_chart(fig2, use_container_width=True)

# Footer
st.markdown("---")
st.caption(f"Dashboard generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — powered by Streamlit & Plotly")
