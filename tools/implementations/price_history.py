import yfinance as yf  # type: ignore
from tools.base import BaseTool
from tools.schemas import PriceHistoryInput


class GetPriceHistory(BaseTool):
    name = "get_price_history"
    description = """
        Fetch historical closing prices for a stock for the last 6 months.
    """
    input_schema = PriceHistoryInput

    def execute(self, **kwargs):
        ticker = kwargs.get("ticker")
        if not isinstance(ticker, str):
            raise ValueError("ticker must be a string")
        
        stock = yf.Ticker(ticker)
        history = stock.history(period="6mo")
        prices = history["Close"].tolist()

        return {
            "prices": prices,
            "latest_price": prices[-1] if prices else None
        }