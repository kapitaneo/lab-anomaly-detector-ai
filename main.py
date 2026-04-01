from agent.agent import run_agent
import json

with open("data/sample_plate.json") as f:
    data = json.load(f)

result = run_agent(data)

try:
    parsed = json.loads(result)
    print("\n=== STRUCTURED RESULT ===")
    print(json.dumps(parsed, indent=2))
except:
    print("\n=== RAW RESULT ===")
    print(result)