# SHORTLISTING OCR ASSIGNMENT

## Objective
A system that extracts structured data fr4om images using OCR and provides confidence aware JSON-Outputs

## Tools & Libraries
- Python 3.12
- Tesseract OCR (pytesseract)
- OpenCV for preprocessing
- Regex (re) for field extraction

## Project Structure
assignment_cc/
├── main.py
├── ocr_eng.py
├── extraction.py
├── confidence.py
├── preprocessing.py
├── utils.py
├── summary.py
├── README.md
└── requirements.txt

# How to Run
```bash
pip install -r requirements.txt
python3 main.py
python3 summary.py

## Approach
1. Images preprocessed for noise, contrast and skew
2. Tesseract OCR extracts text from each receipt
3. Regex patterns extract store name, date, total, items
4. Confidence scores assigned to each field
5. Output saved as structured JSON per receipt
6. Summary generated across all receipts

## Output Format:
{
  "store_name": {"value": "WAL-MART", "confidence": 0.9},
  "date": {"value": "10/20/07", "confidence": 0.88},
  "total_amount": {"value": "18.75", "confidence": 0.95},
  "items": []
}

## Challenges
1. OCR misreads on noisy and blurry receipts
2. Varied date and currency formats across receipts
3. Low contrast images affecting extraction accuracy
## Improvements
1. Fine-tune OCR model for receipt-specific text
2. Use ML-based field extraction instead of regex
3. Add layout analysis for better item detection