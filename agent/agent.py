import json
import os

from openai import OpenAI
from dotenv import load_dotenv

from agent.executor import execute_tool_call
from agent.prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

tools = [
    {
        "type": "function",
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
    },
    {
        "type": "function",
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
    },
    {
        "type": "function",
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
]


def run_agent(data: dict):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"Analyze this lab plate data: {data}"
            }
        ],
        tools=tools
    )

    while True:
        tool_outputs = []

        for item in response.output:
            if item.type == "function_call":
                args = json.loads(item.arguments)

                print(f"[TOOL CALL] {item.name} args={args}")

                result = execute_tool_call(item)
                
                print(f"[TOOL RESULT] {result}")

                tool_outputs.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": result
                })

        if not tool_outputs:
            return response.output_text

        response = client.responses.create(
            model="gpt-4.1-mini",
            previous_response_id=response.id,
            input=tool_outputs
        )
        
        return response.output_text