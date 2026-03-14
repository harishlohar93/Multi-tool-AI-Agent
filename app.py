import streamlit as st
from agent import run_agent
from utils import create_pdf
import time



# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Multi Tool AI Agent",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# Custom Styling
# ---------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

.stChatMessage {
    border-radius: 12px;
    padding: 10px;
}

.stChatInput input {
    border-radius: 20px;
}

.tool-box {
    background-color:#f6f6f6;
    padding:10px;
    border-radius:10px;
    margin-bottom:10px;
}

.activity-box {
    background-color:#fafafa;
    padding:10px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Session State
# ---------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "agent_steps" not in st.session_state:
    st.session_state.agent_steps = []
    
if "last_result" not in st.session_state:
    st.session_state.last_result = None    

if "last_query" not in st.session_state:
    st.session_state.last_query = None     

# ---------------------------
# Layout
# ---------------------------
col1, col2 = st.columns([3,1])

# ---------------------------
# Sidebar
# ---------------------------
with st.sidebar:

    st.title("Agent Control")

    st.subheader("Model : 🧠 LLaMA 3",  )

    st.subheader("🛠 Available Tools")

    st.markdown("""
    🔍 **Web Search**  
    
    📈 **Stock Data**  
    
    📖 **Wikipedia**  
    """)

    st.divider()

    st.subheader("💡 Example Queries")

    st.write("• Analyze Tesla as a company")
    st.write("• What is the stock price of Apple?")
    st.write("• Give me a report on Microsoft")

    st.divider()

    if st.button("🧹 Clear Chat"):
        st.session_state.history = []
        st.rerun()

# ---------------------------
# Chat Panel
# ---------------------------
with col1:

    st.title("🤖OmniSearch AI - Multi-Tool AI Agent")
    st.caption("Research assistant powered by LLaMA 3 + LangChain")

    # Show chat history
    for chat in st.session_state.history:

        with st.chat_message("user"):
            st.write(chat["question"])

        with st.chat_message("assistant"):
            st.markdown(chat["answer"])

    # Chat input
    query = st.chat_input("Ask your AI agent...")
    
   

    def stream_response(text):
        words = text.split()
        streamed_text = ""

        placeholder = st.empty()

        for word in words:
            streamed_text += word + " "
            placeholder.markdown(streamed_text)
            time.sleep(0.08)  # speed of streaming

        return streamed_text

    if query:

        # Display user message
        with st.chat_message("user"):
            st.write(query)

        # Agent response
        with st.chat_message("assistant"):

            with st.status("Agent working...", expanded=True) as status:

                st.write("🔍 Searching web...")
                time.sleep(0.4)
                
                st.write(" OR ")

                st.write("📖 Checking Wikipedia...")
                time.sleep(0.4)
                
                st.write(" OR ")

                st.write("📈 Fetching stock data...")
                time.sleep(0.4)

                result = run_agent(query)

                status.update(label="✅ Research Complete", state="complete")

            final_text = stream_response(result)
            
            # Reasoning expander
            with st.expander("🧠 Agent Reasoning"):
                st.write("""
Step 1: Understand user query  
Step 2: Select appropriate tool  
Step 3: Retrieve data  
Step 4: Analyze results  
Step 5: Generate final answer
                """)
 
        # Save to history
        st.session_state.history.append({
            "question": query,
            "answer": final_text
        })
 
        # Save last result for PDF download
        st.session_state.last_result = final_text
        st.session_state.last_query = query
 
    # ---------------------------
    # PDF Download Button
    # shown after any result exists
    # ---------------------------
    if st.session_state.last_result:
        st.divider()
        if st.button("📄 Generate PDF Report"):
            pdf = create_pdf(
                st.session_state.last_query,
                st.session_state.last_result
            )
            st.download_button(
                label="⬇️ Download Report as PDF",
                data=pdf,
                file_name="research_report.pdf",
                mime="application/pdf"
            )
 