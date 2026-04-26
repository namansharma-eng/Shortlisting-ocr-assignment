import pytesseract

def extract_text(image):
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    text = " ".join(data['text'])
    confidence = data['conf']
    return data, text