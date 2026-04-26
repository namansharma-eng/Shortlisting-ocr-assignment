import json, os

def generate_summary():
    total_spend = 0
    transactions = 0
    store_spend = {}
    
    for f in os.listdir("output"):
        if f.endswith(".json"):
            with open(f"output/{f}") as file:
                data = json.load(file)
            
            transactions += 1
            amount = data.get("total_amount", {}).get("value")
            store = data.get("store_name", {}).get("value", "Unknown")
            
            if amount:
                try:
                    amt = float(str(amount).replace(",",""))
                    total_spend += amt
                    store_spend[store] = store_spend.get(store, 0) + amt
                except: pass
    
    summary = {
        "total_spend": round(total_spend, 2),
        "num_transactions": transactions,
        "spend_per_store": store_spend
    }
    
    with open("summary.json", "w") as f:
        json.dump(summary, f, indent=4)
    
    print(json.dumps(summary, indent=4))

generate_summary()