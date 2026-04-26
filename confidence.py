def get_avg_confidence(results):
    if not results:
        return 0.0
    
    total = 0
    count = 0
    for item in results:
        if len(item) == 3:
            try:
                total += float(item[2])
                count += 1
            except (ValueError, TypeError):
                continue
    return total / count if count > 0 else 0.0
def field_confidence(value, ocr_conf):
    if not value:
        return 0.0
    return ocr_conf