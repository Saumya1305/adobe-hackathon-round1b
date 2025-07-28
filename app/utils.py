# app/utils.py
import fitz  # PyMuPDF
import os
import json

def extract_paragraphs_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    paragraphs = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        lines = page.get_text("text").split('\n')
        for line in lines:
            if len(line.strip()) > 30:
                paragraphs.append({
                    "text": line.strip(),
                    "page": page_num + 1
                })
    return paragraphs

def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
