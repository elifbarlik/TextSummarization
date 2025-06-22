from langdetect import detect
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

import nltk
nltk.download('punkt')

model = SentenceTransformer('all-MiniLM-L6-v2')

def preprocess_emails(emails):
    clean_emails = []
    for email in emails:
        email = email.replace('\n', ' ').strip()
        if detect(email) != 'en':
            continue
        sentences = [s.strip() for s in sent_tokenize(email) if s.strip()]
        clean_emails.append(sentences)
    return clean_emails

def encode_emails(email_sentences):
    all_embeddings = []
    for sentences in email_sentences:
        embeddings = model.encode(sentences)
        all_embeddings.append(embeddings)
    return all_embeddings

def summarize_emails(emails, embeddings, top_n=3):
    summaries = []
    for sent_list, emb_list in zip(emails, embeddings):
        avg_vector = np.mean(emb_list, axis=0)
        sims = cosine_similarity([avg_vector], emb_list)[0]
        top_idx = sims.argsort()[-top_n:][::-1]
        top_sentences = [sent_list[i] for i in sorted(top_idx)]
        summaries.append(' '.join(top_sentences))
    return summaries

