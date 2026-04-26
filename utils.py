import json
import os

def save_json(data, filename):
    os.makedirs("output", exist_ok=True)

    with open(f"output/{filename}", "w") as f:
        json.dump(data, f, indent=2)