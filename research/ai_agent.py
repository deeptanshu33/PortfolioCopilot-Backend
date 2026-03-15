from agents import Agent, Runner, function_tool, WebSearchTool
import numpy as np
import yfinance as yf # type: ignore

from tools.schemas import PortfolioReport  


@function_tool
def get_ticker_fundamentals(ticker: str):
    """
    Fetch financial fundamentals for a company including
    PE ratio, revenue growth, and debt to equity.
    """
    if not isinstance(ticker, str):
        raise ValueError("ticker must be provided as a string")

    stock = yf.Ticker(ticker)
    info = stock.info
    fundamentals = {
        "pe_ratio": info.get("trailingPE"),
        "forward_pe": info.get("forwardPE"),
        "market_cap": info.get("marketCap"),
        "revenue_growth": info.get("revenueGrowth"),
        "debt_to_equity": info.get("debtToEquity"),
    }

    return fundamentals


@function_tool
def get_ticker_price_history(ticker: str):
    """
    Fetch historical closing prices for a stock for the last 6 months.
    """
    if not isinstance(ticker, str):
        raise ValueError("ticker must be a string")

    stock = yf.Ticker(ticker)
    history = stock.history(period="6mo")
    prices = history["Close"].tolist()

    return {"prices": prices, "latest_price": prices[-1] if prices else None}


@function_tool
def get_ticker_price_volatility(ticker: str):
    """
    Compute annualized volatility using daily returns.
    """
    if not isinstance(ticker, str):
        raise ValueError("ticker must be a string")
    stock = yf.Ticker(ticker)
    history = stock.history(period="6mo")
    returns = history["Close"].pct_change().dropna()
    volatility = np.std(returns) * np.sqrt(252)

    return {"annualized_volatility": float(volatility)}


agent = Agent(
    name="portfolio managing expert",
    instructions="You are a portfolio managing expert like Warren Buffet, you will recieve a ticker as input and a thesis regarding it as input. Using the tools provided and your expertise in the matter comment on the provided thesis in the form of a short report, there is no necessity to validated the provided thesis always, be objective and factual. You can search the web to get a pictute of the global economic and political landscape if required. When numerical financial metrics are returned by tools, ALWAYS use those values in your analysis. Do not replace them with numbers from web sources. Web search should only be used for qualitative context like news, macro trends, or analyst sentiment.",

    tools=[
        get_ticker_fundamentals,
        get_ticker_price_history,
        get_ticker_price_volatility,
        WebSearchTool(),
    ],

    output_type=PortfolioReport
)


async def _call_agent_async(thesis: str):
    result = Runner.run_streamed(agent, thesis)
    async for event in result.stream_events():
        if event.type == "raw_response_event":
            continue
        elif event.type == "agent_updated_stream_event":
            continue
        elif event.type == "run_item_stream_event":
            if event.item.type == "tool_call_item":
                raw = event.item.raw_item
                # Try common attribute names first, then dict keys, and finally fall back to the raw type name
                tool_name = None
                if isinstance(raw, dict):
                    tool_name = raw.get("name") or raw.get("tool_name")
                else:
                    tool_name = getattr(raw, "name", None) or getattr(raw, "tool_name", None) or getattr(raw, "tool", None)
                print(f"Tool called: {tool_name or type(raw).__name__}")
            else:
                pass  # Ignore other event types
    return result.final_output.model_dump()

