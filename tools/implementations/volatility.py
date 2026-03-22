import yfinance as yf  # type: ignore
from tools.base import BaseTool
import numpy as np

# from tools.schemas import VolatilityInput


class ComputeVolatilityTool(BaseTool):
    name = "compute_volatility"
    description = """
    Compute annualized volatility using daily returns.
    """
    # input_schema = VolatilityInput

    def execute(self, **kwargs):
        ticker = kwargs.get("ticker")
        if not isinstance(ticker, str):
            raise ValueError("ticker must be a string")
        stock = yf.Ticker(ticker)
        history = stock.history(period="6mo")
        returns = history["Close"].pct_change().dropna()
        volatility = np.std(returns) * np.sqrt(252)

        return {
            "annualized_volatility": float(volatility)
        }
