# Adobe Semantic Linker (Round 1B - Connecting the Dots Hackathon)

This project extracts semantic links from a PDF file. It identifies meaningful relationships between sentences or passages across different pages and returns them in structured JSON format.

## Problem Statement

Given a PDF, the task is to detect and output semantically related content across sections. Each link includes:
- Source and target sentences
- Page numbers for both
- A semantic similarity score

## Folder Structure

round1b/
├── Dockerfile
├── requirements.txt
├── main.py
├── utils.py
├── analyze.py
├── app/
│   ├── input/
│   │   ├── paper.pdf
│   │   ├── persona.json
│   ├── output/
│   │   └── challenge1b_output.json   ← (generated after run)
│   ├── model/
│   │   └── paraphrase-MiniLM-L6-v2/  ← offline saved model directory


## How to Run (Using Docker)

Make sure Docker is installed and running.

### 1. Clone the repository
git clone https://github.com/your-username/adobe-semantic-linker.git
cd adobe-semantic-linker


### 2. Add your PDF file
Place a test file (e.g., sample.pdf) inside the input/ folder.

### 3. Build the Docker image
docker build --platform linux/amd64 -t adobe-semantic-linker .


### 4. Run the container

*On Mac/Linux:*
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none adobe-semantic-linker


*On Windows CMD:*
docker run --rm -v %cd%/input:/app/input -v %cd%/output:/app/output --network none adobe-semantic-linker


The output/result.json file will contain the extracted semantic links.

## Example Output

json
{
  "title": "paper",
  "semantic_links": [
    {
      "source": {
        "text": "Page 1: Artificial Intelligence (AI) is the simulation of human intelligence in machines.",
        "page": 1
      },
      "target": {
        "text": "AI systems are designed to perform tasks such as recognizing speech, learning, and",
        "page": 1
      },
      "score": 0.61
    }
  ]
}


## Technologies Used

* Python 3.10
* Sentence-Transformers (BERT-based models)
* PyMuPDF for PDF parsing
* Docker for containerization

## Submission Checklist

* Dockerfile in root folder
* All dependencies installed inside container
* Offline execution (no network calls)
* No hardcoded values
* Supports PDF input from /app/input
* Output saved to /app/output in required JSON format
* CPU optimized processing

## Team Info

* *Team Name:* Maestro
* *Hackathon:* Adobe India – "Connecting the Dots"
* *Round:* 1B – Semantic Link Extraction
