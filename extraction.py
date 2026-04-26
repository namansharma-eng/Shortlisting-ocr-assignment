import re

def extract_fields(data):
    if isinstance(data, tuple):
        text = ' '.join(str(w) for w in data if str(w).strip())
    elif isinstance(data, dict):
        words = data.get("text", [])
        text = ' '.join(str(w) for w in words if str(w).strip())
    else:
        text = str(data)

    lines = text.split('\n')

    store_match = re.search(r'[A-Z][A-Z\s\*\-]{3,}', text)
    store_name = store_match.group(0).strip() if store_match else None

    # Date - multiple formats
    date_match = re.search(r'\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4}', text)
    date = date_match.group(0) if date_match else None

    # Total
    total_match = re.search(r'(TOTAL|AMOUNT|GRAND TOTAL|JUMLAH)\s*:?\s*(\d+\.\d{2})', text, re.IGNORECASE)
    total_amount = total_match.group(2) if total_match else None

    # Items
    items = []
    item_matches = re.findall(r'([A-Z][A-Z\s]+?)\s+(\d+\.\d{2})', text)
    for name, price in item_matches:
        if 'TOTAL' not in name and 'TAX' not in name:
            items.append({"name": name.strip(), "price": price})

    return {
        "store_name": store_name,
        "date": date,
        "total_amount": total_amount,
        "items": items
    }