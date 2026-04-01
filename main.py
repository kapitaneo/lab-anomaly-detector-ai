from agent.agent import run_agent
import json

with open("data/sample_plate.json") as f:
    data = json.load(f)

result = run_agent(data)

print("\n=== AGENT RESULT ===")
print(result)