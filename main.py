import os
from preprocessing import preprocess_image
from ocr_eng import extract_text
from extraction import extract_fields
from confidence import get_avg_confidence, field_confidence
from utils import save_json

IMAGE_FOLDER = "images"

def process_receipt(image_path):
    processed = preprocess_image(image_path)
    results, text = extract_text(processed)

    extracted = extract_fields(text)
    ocr_conf = get_avg_confidence(results)

    final_output = {
        "store_name": {
            "value": extracted["store_name"],
            "confidence": field_confidence(extracted["store_name"], ocr_conf)
        },
        "date": {
            "value": extracted["date"],
            "confidence": field_confidence(extracted["date"], ocr_conf)
        },
        "items": extracted["items"],
        "total_amount": {
            "value": extracted["total_amount"],
            "confidence": field_confidence(extracted["total_amount"], ocr_conf)
        }
    }
    return final_output

def main():
    for filename in os.listdir(IMAGE_FOLDER):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            path = os.path.join(IMAGE_FOLDER, filename)
            result = process_receipt(path)
            save_json(result, filename.split('.')[0] + '.json')
            print("Processed:", filename)

if __name__ == "__main__":
    main()