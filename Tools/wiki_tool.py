import os
from langchain.tools import tool
import wikipedia


@tool
def wikipedia_tool(query: str) -> str:
    """
    Retrieve a short summary of a topic from Wikipedia.
    Input should be a person, place, company, concept, or event.
    Returns a concise description from Wikipedia.
    """
    
    try: 
        summary = wikipedia.summary(query, sentences=5)

        result = f"""
Wikipedia Summary for {query}
------------------------------------
{summary}
"""
        return result.strip()

    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found. Try being more specific. Examples: {e.options[:5]}"

    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found for this query."

    except Exception as e:
        return f"Search failed: {str(e)}"


# Standalone test
if __name__ == "__main__":
    result = wikipedia_tool.invoke("Apple Inc")
    print(result)