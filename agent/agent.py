import json
import os

from openai import OpenAI
from dotenv import load_dotenv

from agent.tools import check_threshold, detect_borderline, detect_outliers

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

tools = [
    {
        "type": "function",
        "function": {
            "name": "check_threshold",
            "description": "Check if sample value exceeds threshold",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {"type": "number"},
                    "threshold": {"type": "number"}
                },
                "required": ["value", "threshold"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "detect_borderline",
            "description": "Detect if value is close to threshold",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {"type": "number"},
                    "threshold": {"type": "number"}
                },
                "required": ["value", "threshold"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "detect_outliers",
            "description": "Detect outliers across samples",
            "parameters": {
                "type": "object",
                "properties": {
                    "values": {
                        "type": "array",
                        "items": {"type": "number"}
                    }
                },
                "required": ["values"]
            }
        }
    }
]


def run_agent(data: dict):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Analyze this lab plate data: {data}",
        tools=tools
    )

    while True:
        tool_outputs = []

        for item in response.output:
            if item.type == "function_call":
                args = json.loads(item.arguments)

                if item.name == "check_threshold":
                    result = args["value"] > args["threshold"]

                elif item.name == "detect_borderline":
                    result = abs(args["value"] - args["threshold"]) < 0.2

                elif item.name == "detect_outliers":
                    values = args["values"]
                    avg = sum(values) / len(values)
                    result = [
                        v for v in values if abs(v - avg) > 1.5
                    ]

                else:
                    result = "unknown tool"

                tool_outputs.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": str(result)
                })

        if tool_outputs:
            response = client.responses.create(
                model="gpt-4.1-mini",
                previous_response_id=response.id,
                input=tool_outputs
            )
            continue

        return response.output_text