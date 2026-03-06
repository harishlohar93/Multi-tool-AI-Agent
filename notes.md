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

