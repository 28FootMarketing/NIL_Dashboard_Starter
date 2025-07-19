import streamlit as st
import requests
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="NIL Agent Assistant",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">🏆 NIL Agent Assistant</h1>', unsafe_allow_html=True)
st.markdown("### Get expert guidance on Name, Image, and Likeness challenges")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if 'query_count' not in st.session_state:
    st.session_state.query_count = 0

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    webhook_url = st.text_input(
        "N8N Webhook URL",
        placeholder="https://your-n8n-instance.com/webhook/nil-agent",
        help="Enter the full URL of your N8N webhook endpoint"
    )
    
    st.markdown("---")
    
    st.subheader("🔧 API Settings")
    timeout_duration = st.slider("Request Timeout (seconds)", 5, 30, 15)
    
    st.markdown("---")
    
    st.subheader("📊 Session Stats")
    st.metric("Queries Made", st.session_state.query_count)
    
    if st.button("Reset Session", type="secondary"):
        st.session_state.query_count = 0
        st.session_state.messages = []
        st.rerun()

def call_nil_agent(query, webhook_url, timeout_duration):
    """Make API call to N8N webhook"""
    try:
        payload = {"query": query}
        
        response = requests.post(
            webhook_url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=timeout_duration
        )
        
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.Timeout:
        return {"success": False, "error": "Request timed out. Please try again."}
    except requests.exceptions.ConnectionError:
        return {"success": False, "error": "Failed to connect to the NIL Agent API. Please check the webhook URL."}
    except requests.exceptions.HTTPError as e:
        return {"success": False, "error": f"HTTP error occurred: {e}"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": f"Request failed: {e}"}
    except json.JSONDecodeError:
        return {"success": False, "error": "Invalid JSON response from API"}

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            if "data" in message:
                data = message["data"]
                if data.get("success"):
                    st.markdown(f"**Problem:** {data.get('problem_title', 'N/A')}")
                    if data.get("problem_found"):
                        st.markdown(f"**Category:** {data.get('problem_category', 'General')}")
                        st.markdown(f"**Description:** {data.get('problem_description', 'N/A')}")
                    st.markdown("**AI Response:**")
                    st.markdown(data.get("ai_response", "No response available"))
                else:
                    st.error(f"Error: {data.get('error', 'Unknown error occurred')}")
            else:
                st.markdown(message["content"])
        else:
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask your NIL question here..."):
    if not webhook_url:
        st.error("⚠️ Please enter your N8N webhook URL in the sidebar before asking questions.")
        st.stop()
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Consulting NIL database and AI..."):
            response_data = call_nil_agent(prompt, webhook_url, timeout_duration)
            
            st.session_state.query_count += 1
            
            if response_data.get("success"):
                st.markdown(f"**Problem Found:** {response_data.get('problem_title', 'N/A')}")
                
                if response_data.get("problem_found"):
                    st.success("✅ Matched to existing NIL problem in database")
                    st.markdown(f"**Description:** {response_data.get('problem_description', 'N/A')}")
                else:
                    st.info("ℹ️ No specific match found - providing general NIL guidance")
                
                st.markdown("**AI Response:**")
                ai_response = response_data.get("ai_response", "No response available")
                st.markdown(ai_response)
                
                st.caption(f"Response generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": ai_response,
                    "data": response_data
                })
                
            else:
                error_msg = response_data.get("error", "Unknown error occurred")
                st.error(f"❌ {error_msg}")
                
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": f"Sorry, I encountered an error: {error_msg}",
                    "data": response_data
                })

# Information section
with st.expander("ℹ️ How to use this NIL Agent"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Getting Started:**
        1. Enter your N8N webhook URL in the sidebar
        2. Ask any NIL-related question in the chat
        3. Get AI-powered responses based on the NIL database
        
        **Example Questions:**
        - "What are the rules for athlete endorsements?"
        - "Can I sell my autographs as a student athlete?"
        - "How do NIL deals affect my scholarship?"
        """)
    
    with col2:
        st.markdown("""
        **Features:**
        - 🔍 Smart problem matching from NIL database
        - 🤖 AI-generated responses using GPT-4
        - 📊 Session statistics tracking
        - ⚡ Real-time API integration with N8N
        - 💬 Chat-style interface for easy interaction
        
        **Need Help?**
        Check your N8N webhook URL and ensure the workflow is active.
        """)

# Footer
st.markdown("---")
st.markdown("🔗 **Powered by N8N Workflow** | Built with Streamlit | NIL Agent Assistant v1.0")
