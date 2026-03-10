import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from Tools.tavily_tool import search_tool
from Tools.stock_tool import finance_tool
from Tools.wiki_tool import wikipedia_tool

# Load environment variables
load_dotenv()

# Validate API key
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

# ── 1. Initialize LLM ──────────────────────────────────────
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=1024,
    max_retries=2,
)

# ── 2. Define Tools List ────────────────────────────────────
tools = [search_tool, finance_tool, wikipedia_tool]

# ── 3. Pull ReAct Prompt from LangChain Hub ─────────────────
prompt = hub.pull("hwchase17/react")

# ── 4. Create the Agent ─────────────────────────────────────
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

# ── 5. Memory ───────────────────────────────────────────────
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)

# ── 6. Create Agent Executor ────────────────────────────────
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=5,
    
)


# ── 7. Run Function ─────────────────────────────────────────
def run_agent(query: str) -> str:
    """
    Run the agent with a given query.
    Returns the final response as a string.
    """
     # Handle identity questions directly
    identity_keywords = ["your name", "who are you", "what are you", "about you", "who built you", "what is your name"]
    if any(keyword in query.lower() for keyword in identity_keywords):
        return "I'm **OmniSearch AI**, a Multi-Tool AI Research Agent built by Harish Lohar (Pre final year engineering student). I can help you research companies, get stock prices, search the web, and find Wikipedia summaries. Try asking me to analyze a company!"
    try:
        response = agent_executor.invoke({"input": query})
        return response.get("output", "No response generated.")
    except Exception as e:
        return f"Agent failed: {str(e)}"


# ── 8. Standalone Test ──────────────────────────────────────
if __name__ == "__main__":

    # Test 1 — Simple query (should use wiki_tool)
    print("\n" + "="*50)
    print("TEST 1: Simple Wikipedia query")
    print("="*50)
    result = run_agent("What is artificial intelligence?")
    print("\nFinal Answer:", result)

    # Test 2 — Financial query (should use finance_tool)
    print("\n" + "="*50)
    print("TEST 2: Financial query")
    print("="*50)
    result = run_agent("What is the current stock price of Apple?")
    print("\nFinal Answer:", result)

    # Test 3 — Multi tool query (should use all 3 tools)
    print("\n" + "="*50)
    print("TEST 3: Full research report")
    print("="*50)
    result = run_agent("Give me a complete research report on Tesla Inc")
    print("\nFinal Answer:", result)