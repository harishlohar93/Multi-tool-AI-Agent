## Day 1 Notes

### What I built:
- search_tool using Tavily API
- finance_tool using yfinance
- wiki_tool using Wikipedia library

### What I learned:
- @tool decorator wraps function for LangChain agent
- Docstring is what the LLM reads to decide which tool to use
- .info is a property not a method (no brackets)
- Each tool must return a string
- try/except prevents agent from crashing


### What I figured out myself:
- query.upper() for ticker symbols
- if not r: check for empty data
- 3 different exception types in wiki_tool


## Day 2 Notes

### What I built:
- agent.py connecting all 3 tools to LangChain AgentExecutor

### What I saw working:
- ReAct pattern: Thought → Action → Observation → Final Answer
- Agent autonomously picked correct tool for each query
- All 3 tools fired together on Tesla research query

### What I learned:
- create_react_agent builds the agent
- AgentExecutor runs the loop
- hub.pull downloads the ReAct thinking prompt
- Agent picks tools based on docstrings
- verbose=True shows live reasoning

### Key versions that work:
- langchain==0.2.16
- langchain-groq==0.1.9
- model: llama-3.3-70b-versatile


## Day 3 Notes

### What I built:
- Complete Streamlit UI for OmniSearch AI agent
- Dark theme with custom CSS styling
- Two column layout with sidebar
- Chat history using session_state
- st.status() box showing agent working steps
- Streaming response effect word by word
- Agent reasoning expander
- Agent identity handling 


### What I learned:
- How session_state works — survives reruns
- Why Streamlit reruns entire file on every interaction
- st.chat_input() vs st.text_input() difference
- st.status() for live progress updates
- st.chat_message() creates chat bubbles
- stream_response() function for typing effect
- set_page_config() must be first Streamlit command

### What I figured out myself:
- Added custom CSS for border radius and padding
- Used st.columns() for layout
- Clear chat button with st.rerun()

### What confused me:
- session_state initialization order matters
- PDF button placement outside query block

---

## Day 4 Notes

### What I built:
- utils.py with create_pdf() function
- PDF export feature using reportlab
- Download button using st.download_button()
- Fixed session_state for last_result and last_query
- In-memory PDF generation using io.BytesIO()

### What I learned:
- reportlab creates PDFs programmatically
- io.BytesIO() generates PDF in memory — no file saved to disk
- st.download_button() needs bytes data
- buffer.seek(0) resets buffer position before reading
- Markdown symbols must be stripped before writing to PDF
- session_state persists data between Streamlit reruns

### What I figured out myself:
- last_result and last_query saved to session_state
  so PDF button works even after page reruns

### What confused me:
- session_state AttributeError — must initialize
  ALL variables at top before using anywhere

### Key insight:
- In Streamlit, every button click reruns the entire file
- That's why session_state exists — to remember things
  across those reruns

  ## Day 5 Notes

### What I built:
- Dockerfile for containerizing the app
- .dockerignore to exclude unnecessary files
- docker-compose.yml for easy local Docker setup
- Successfully built and ran app inside Docker container

### What I learned:
- Docker packages entire environment into a container
- FROM python:3.11-slim is the correct base image
- WORKDIR /app sets working directory inside container
- COPY requirements.txt first — Docker caches this layer
- EXPOSE 8501 opens the Streamlit port
- CMD runs the app when container starts
- --server.address=0.0.0.0 required so app is accessible outside container
- .dockerignore works like .gitignore — excludes .env, .venv, __pycache__
- docker build -t name . builds the image
- docker run -p 8501:8501 --env-file .env runs the container
- Image names must be lowercase — Docker doesn't accept uppercase

### Errors I fixed:
- Docker daemon not running → opened Docker Desktop first
- python:3.11.9-slim-bookwor → wrong image name, fixed to python:3.11-slim
- langchain-hub → doesn't exist as package, removed from requirements.txt
- reportlab-4.4.10 → version doesn't exist, removed version number

### What I figured out myself:
- Railway auto-detects Dockerfile from GitHub repo
- Environment variables must be added manually on Railway
- Same Docker container runs locally and on Railway

### Key insight:
- Docker solves "works on my laptop" problem
- Container = your entire environment in a box
- Any server can run the same container identically