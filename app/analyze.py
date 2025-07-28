# app/analyze.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('/app/model/paraphrase-MiniLM-L6-v2')

def link_semantic_paragraphs(paragraphs, threshold=0.6):
    texts = [p['text'] for p in paragraphs]
    embeddings = model.encode(texts)
    links = []

    for i in range(len(embeddings)):
        for j in range(i + 1, len(embeddings)):
            score = cosine_similarity([embeddings[i]], [embeddings[j]])[0][0]
            if score >= threshold:
                links.append({
                    "source": {
                        "text": paragraphs[i]["text"],
                        "page": paragraphs[i]["page"]
                    },
                    "target": {
                        "text": paragraphs[j]["text"],
                        "page": paragraphs[j]["page"]
                    },
                    "score": round(float(score), 2)
                })
    return links
