import json
from agent.tools import TOOL_REGISTRY


def execute_tool_call(item):
    args = json.loads(item.arguments)

    fn = TOOL_REGISTRY.get(item.name)

    if not fn:
        return "unknown tool"

    try:
        return fn(**args)
    except Exception as e:
        return f"error: {str(e)}"