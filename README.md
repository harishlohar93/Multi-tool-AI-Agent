# 🤖 OmniSearch AI — Multi-Tool AI Research Agent

A ReAct-based AI agent that autonomously selects and uses multiple 
real-time tools to research any topic and generate structured reports 
in under 30 seconds.

🚀 **Live Demo:** [multi-tool-ai-agent-production.up.railway.app](https://multi-tool-ai-agent-production.up.railway.app)

---

## ✨ Features

- 🔍 **Web Search** — Real-time search via Tavily API
- 📈 **Stock Data** — Live financial data via yfinance
- 📖 **Wikipedia** — Instant topic summaries
- 🧠 **Multi-turn Memory** — Remembers conversation context
- 📄 **PDF Export** — Download research reports instantly
- 🐳 **Dockerized** — Runs consistently anywhere
- ⚡ **Streaming Responses** — Word-by-word live output

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | LLaMA 3 70B via Groq API |
| Agent Framework | LangChain (ReAct pattern) |
| Web Search | Tavily API |
| Financial Data | yfinance |
| Knowledge Base | Wikipedia |
| Frontend | Streamlit |
| PDF Generation | ReportLab |
| Containerization | Docker |
| Deployment | Railway |

---

## 🏗️ Project Structure
```
📂 Multi-tool-AI-Agent/
├── 📄 agent.py            ← LangChain ReAct agent
├── 📄 app.py              ← Streamlit UI
├── 📄 utils.py            ← PDF generation
├── 📄 Dockerfile          ← Docker config
├── 📄 docker-compose.yml  ← Local Docker setup
├── 📄 requirements.txt
├── 📄 .env
└── 📂 Tools/
    ├── 📄 tavily_tool.py  ← Web search tool
    ├── 📄 stock_tool.py   ← Finance tool
    └── 📄 wiki_tool.py    ← Wikipedia tool
```

---

## ⚙️ How It Works
```
User Query
    ↓
LangChain ReAct Agent (LLaMA 3 70B)
    ↓
Decides which tool to use
    ↓
┌─────────────┬──────────────┬─────────────┐
│ Tavily      │  yfinance    │  Wikipedia  │
│ Web Search  │  Stock Data  │  Summaries  │
└─────────────┴──────────────┴─────────────┘
    ↓
Synthesizes results
    ↓
Structured Research Report
    ↓
Optional PDF Export
```

---

## 🚀 Run Locally

### Option 1 — Python
```bash
# Clone repo
git clone https://github.com/harishlohar93/Multi-tool-AI-Agent
cd Multi-tool-AI-Agent

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Add API keys
cp .env.example .env
# Edit .env with your keys

# Run
streamlit run app.py
```

### Option 2 — Docker
```bash
docker build -t multi-tool-ai-agent .
docker run -p 8501:8501 --env-file .env multi-tool-ai-agent
```

Open: `http://localhost:8501`

---

## 🔑 Environment Variables

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get free API keys:
- Groq: [console.groq.com](https://console.groq.com)
- Tavily: [tavily.com](https://tavily.com)

---

## 💬 Example Queries
```
"Give me a research report on Tesla"
"What is the current stock price of Apple?"
"Who is Sundar Pichai?"
"Latest news on artificial intelligence"
"Compare Google and Microsoft"
```

---

## 📸 Demo

> Ask any question → agent picks the right tool → 
> get a full research report → download as PDF

---

## 👨‍💻 Author

**Harish Lohar**
- GitHub: [github.com/harishlohar93](https://github.com/harishlohar93)
- LinkedIn: [linkedin.com/in/harishlohar](https://www.linkedin.com/in/hlohar)

---

## 📄 License

MIT License