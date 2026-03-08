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

