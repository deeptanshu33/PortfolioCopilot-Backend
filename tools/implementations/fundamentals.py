from tools.base import BaseTool
import yfinance as yf #type: ignore

from tools.schemas import FundamentalsInput 

class GetFundamentalsTool(BaseTool):
    name = "get_fundamentals"
    description = '''
    Fetch financial fundamentals for a company including
    PE ratio, revenue growth, and debt to equity.
    '''
    input_schema = FundamentalsInput

    def execute(self, **kwargs):
        ticker = kwargs.get("ticker")

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