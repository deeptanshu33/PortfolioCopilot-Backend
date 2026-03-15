from tools.registry import TOOLS
def build_open_ai_tool(tool):
    schema = tool.input_schema.model_json_schema()
    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "parameters": schema
        }
    }

def get_open_ai_tools():
    return [
        build_open_ai_tool(tool) for tool in TOOLS.values()
    ]