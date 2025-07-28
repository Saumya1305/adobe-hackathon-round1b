# app/main.py
import os
import json
from utils import extract_paragraphs_from_pdf, save_json
from analyze import link_semantic_paragraphs

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"
INTERMEDIATE_DIR = os.path.join(OUTPUT_DIR, "extracted_texts")

def process():
    for file in os.listdir(INPUT_DIR):
        if file.endswith(".pdf"):
            file_path = os.path.join(INPUT_DIR, file)
            title = file.replace(".pdf", "")

            # Extract
            paragraphs = extract_paragraphs_from_pdf(file_path)
            save_json(paragraphs, os.path.join(INTERMEDIATE_DIR, title + "_paragraphs.json"))

            # Link
            links = link_semantic_paragraphs(paragraphs)

            # Final output
            final_output = {
                "title": title,
                "semantic_links": links
            }
            save_json(final_output, os.path.join(OUTPUT_DIR, "challenge1b_output.json"))

if __name__ == "__main__":
    process()
