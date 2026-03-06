import os
from langchain.tools import tool
import yfinance as yf


@tool
def finance_tool(query: str) -> str:
    """
    Retrieve financial stock information for a company using its ticker symbol.
    Returns current price, market cap, PE ratio, sector, company summary,
    and 52-week high and low.
    """
    try:
        stock = yf.Ticker(query.upper())
        r = stock.info

        if not r:
            return "No stock data found. Please check the ticker symbol."

        result = f"""
Stock Information for {query.upper()}
------------------------------------
Current Price: {r.get('currentPrice')}
Market Cap: {r.get('marketCap')}
PE Ratio: {r.get('trailingPE')}
Sector: {r.get('sector')}
Business Summary: {r.get('longBusinessSummary')}
52 Week High: {r.get('fiftyTwoWeekHigh')}
52 Week Low: {r.get('fiftyTwoWeekLow')}
"""
        return result.strip()

    except Exception as e:
        return f"Search failed: {str(e)}"


# Standalone test
if __name__ == "__main__":
    result = finance_tool.invoke("AAPL")
    print(result)