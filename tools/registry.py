from tools.implementations.fundamentals import GetFundamentalsTool
from tools.implementations.price_history import GetPriceHistory
from tools.implementations.volatility import ComputeVolatilityTool

TOOLS = {
    "get_fundamentals": GetFundamentalsTool(),
    "get_price_history": GetPriceHistory(),
    "compute_volatility": ComputeVolatilityTool()
}

def get_tool(tool_name: str):
    return TOOLS.get(tool_name)