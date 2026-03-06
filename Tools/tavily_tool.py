import os
from dotenv import load_dotenv
from langchain.tools import tool
from tavily import TavilyClient

load_dotenv()

@tool
def search_tool(query: str) -> str:
    """
    Search the web for current news, recent events, or
    any topic that needs up to date information. Input
    should be a specific search query string.
    """
    try:
        client = TavilyClient(os.getenv("TAVILY_API_KEY"))
        response = client.search(query, max_results=3, search_depth="advanced")
        
        formatted_results = []
        for r in response["results"]:
            text = f"Title: {r['title']}\nContent: {r['content']}\nSource: {r['url']}"
            formatted_results.append(text)
        
        return "\n\n".join(formatted_results)
    
    except Exception as e:
        return f"Search failed: {str(e)}"


# Standalone test
if __name__ == "__main__":
    result = search_tool.invoke("Who is Virat Kohli?")
    print(result)