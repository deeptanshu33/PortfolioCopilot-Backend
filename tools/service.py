from research.models import ToolLog
from tools.registry import get_tool
import time

def execute_tool(tool_name, report, **kwargs):
    tool = get_tool(tool_name)

    start = time.time()
    result = tool.execute(**kwargs)
    duration = time.time() - start

    ToolLog.objects.create(
        report = report,
        tool_name = tool_name,
        input_payload = kwargs,
        output_payload = result,
        execution_time = duration
    )

    return result