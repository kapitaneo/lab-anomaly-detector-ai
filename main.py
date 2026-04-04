from agent.agent import run_agent
import json

def evaluate_result(result_json):
    issues = result_json.get("anomalies", [])
    
    if len(issues) == 0:
        return "No anomalies detected"
    
    return f"{len(issues)} anomalies detected"

with open("data/sample_plate.json") as f:
    data = json.load(f)

result = run_agent(data)

try:
    parsed = json.loads(result)
    print("\n=== STRUCTURED RESULT ===")
    print("\n=== EVALUATION ===")
    print(evaluate_result(parsed))
except:
    print("\n=== RAW RESULT ===")
    print(result)