import streamlit as st
import requests
import json
import time

# Page configuration
st.set_page_config(
    page_title="NIL Agent - AI Assistant",
    page_icon="🏈",
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
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    .query-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid #e0e6ed;
    }
    
    .response-box {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #667eea;
    }
    
    .sidebar-content {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    .status-success {
        color: #28a745;
        font-weight: bold;
    }
    
    .status-error {
        color: #dc3545;
        font-weight: bold;
    }
    
    .status-loading {
        color: #ffc107;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🏈 NIL Agent Assistant</h1>', unsafe_allow_html=True)
    st.markdown("**Get AI-powered guidance for your Name, Image, and Likeness opportunities**")
    
    # Sidebar configuration
    with st.sidebar:
        st.markdown("## ⚙️ Configuration")
        
        # N8N Webhook URL configuration
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.markdown("### 🔗 N8N Webhook Settings")
        
        # Default webhook URL from your n8n workflow
        default_webhook_url = "https://your-n8n-instance.com/webhook/ca17d568-b816-40d9-a06b-e498e8659750"
        
        webhook_url = st.text_input(
            "N8N Webhook URL",
            value=default_webhook_url,
            help="Enter your n8n webhook URL here"
        )
        
        # Test connection button
        if st.button("🔍 Test Connection"):
            test_connection(webhook_url)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Recent queries
        st.markdown("### 📝 Recent Queries")
        if 'query_history' in st.session_state and st.session_state.query_history:
            for i, query in enumerate(reversed(st.session_state.query_history[-5:])):
                if st.button(f"💭 {query[:30]}...", key=f"recent_{i}"):
                    st.session_state.current_query = query
                    st.experimental_rerun()
        
        # Clear history
        if st.button("🗑️ Clear History"):
            st.session_state.query_history = []
            st.success("History cleared!")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Query input section
        st.markdown('<div class="query-box">', unsafe_allow_html=True)
        st.markdown("## 💬 Ask Your NIL Question")
        
        # Initialize session state
        if 'query_history' not in st.session_state:
            st.session_state.query_history = []
        if 'current_query' not in st.session_state:
            st.session_state.current_query = ""
        
        # Query input
        user_query = st.text_area(
            "What NIL challenge are you facing?",
            value=st.session_state.current_query,
            height=100,
            placeholder="e.g., 'I'm struggling with brand attention' or 'How can I improve my social media engagement?'"
        )
        
        # Submit button
        col_submit, col_clear = st.columns([1, 1])
        
        with col_submit:
            submit_button = st.button("🚀 Get AI Guidance", type="primary", use_container_width=True)
        
        with col_clear:
            if st.button("🔄 Clear Query", use_container_width=True):
                st.session_state.current_query = ""
                st.experimental_rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Process query
        if submit_button and user_query.strip():
            process_query(user_query.strip(), webhook_url)
        elif submit_button:
            st.warning("⚠️ Please enter a query before submitting.")
    
    with col2:
        # Example queries
        st.markdown("## 💡 Example Queries")
        
        example_queries = [
            "I'm struggling with brand attention",
            "My social media has low visibility",
            "How can I improve engagement?",
            "I need help with content strategy",
            "Brand partnerships aren't working",
            "My follower count is stagnant"
        ]
        
        st.markdown("Click any example to try it:")
        
        for query in example_queries:
            if st.button(f"💭 {query}", key=f"example_{query}", use_container_width=True):
                st.session_state.current_query = query
                st.experimental_rerun()

def test_connection(webhook_url):
    """Test the n8n webhook connection"""
    try:
        # Test with a simple query
        test_payload = {"query": "test connection"}
        
        with st.spinner("Testing connection..."):
            response = requests.post(
                webhook_url,
                json=test_payload,
                timeout=10,
                headers={'Content-Type': 'application/json'}
            )
        
        if response.status_code == 200:
            st.success("✅ Connection successful!")
            st.json(response.json())
        else:
            st.error(f"❌ Connection failed. Status code: {response.status_code}")
            st.text(f"Response: {response.text}")
            
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Connection error: {str(e)}")
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")

def process_query(query, webhook_url):
    """Process user query through n8n workflow"""
    
    # Add to history
    if query not in st.session_state.query_history:
        st.session_state.query_history.append(query)
    
    # Prepare payload for n8n webhook
    payload = {"query": query}
    
    # Create placeholder for status updates
    status_placeholder = st.empty()
    response_placeholder = st.empty()
    
    try:
        # Show loading status
        status_placeholder.markdown(
            '<p class="status-loading">🔄 Processing your query...</p>', 
            unsafe_allow_html=True
        )
        
        # Send request to n8n webhook
        with st.spinner("Getting AI response..."):
            response = requests.post(
                webhook_url,
                json=payload,
                timeout=30,
                headers={'Content-Type': 'application/json'}
            )
        
        if response.status_code == 200:
            # Success
            status_placeholder.markdown(
                '<p class="status-success">✅ Response received successfully!</p>', 
                unsafe_allow_html=True
            )
            
            # Parse response
            try:
                response_data = response.json()
                display_response(response_data, response_placeholder)
            except json.JSONDecodeError:
                # Handle plain text response
                response_placeholder.markdown(
                    f'<div class="response-box"><h3>🤖 AI Response</h3><p>{response.text}</p></div>',
                    unsafe_allow_html=True
                )
        else:
            # Error response
            status_placeholder.markdown(
                f'<p class="status-error">❌ Error: Status code {response.status_code}</p>', 
                unsafe_allow_html=True
            )
            st.error(f"Response: {response.text}")
            
    except requests.exceptions.Timeout:
        status_placeholder.markdown(
            '<p class="status-error">⏱️ Request timed out. Please try again.</p>', 
            unsafe_allow_html=True
        )
    except requests.exceptions.RequestException as e:
        status_placeholder.markdown(
            f'<p class="status-error">🔌 Connection error: {str(e)}</p>', 
            unsafe_allow_html=True
        )
    except Exception as e:
        status_placeholder.markdown(
            f'<p class="status-error">💥 Unexpected error: {str(e)}</p>', 
            unsafe_allow_html=True
        )

def display_response(response_data, placeholder):
    """Display the AI response in a formatted way"""
    
    # Response container
    response_html = '<div class="response-box">'
    response_html += '<h3>🤖 AI Response</h3>'
    
    # Handle different response formats
    if isinstance(response_data, dict):
        # Check for specific fields from your n8n workflow
        if 'ai_response' in response_data:
            response_html += f'<p><strong>AI Guidance:</strong></p><p>{response_data["ai_response"]}</p>'
        
        if 'title' in response_data:
            response_html += f'<p><strong>Problem Area:</strong> {response_data["title"]}</p>'
        
        if 'match_found' in response_data:
            if response_data.get('match_found'):
                response_html += '<p><span style="color: green;">✅ Problem match found in database</span></p>'
            else:
                response_html += '<p><span style="color: orange;">⚠️ No exact match found, using general guidance</span></p>'
        
        # Display any other fields
        for key, value in response_data.items():
            if key not in ['ai_response', 'title', 'match_found'] and not key.startswith('_'):
                if isinstance(value, (str, int, float)):
                    response_html += f'<p><strong>{key.replace("_", " ").title()}:</strong> {value}</p>'
    
    else:
        # Handle string response
        response_html += f'<p>{response_data}</p>'
    
    response_html += '</div>'
    
    placeholder.markdown(response_html, unsafe_allow_html=True)
    
    # Add download button for the response
    if isinstance(response_data, dict):
        st.download_button(
            label="💾 Download Response",
            data=json.dumps(response_data, indent=2),
            file_name=f"nil_response_{int(time.time())}.json",
            mime="application/json"
        )

# Footer
def add_footer():
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 1rem;'>
            <p>🏈 NIL Agent Assistant | Powered by AI & N8N</p>
            <p><small>Connect your athletic brand with the right opportunities</small></p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
    add_footer()
