from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import preprocess_emails, encode_emails, summarize_emails

app = FastAPI()
import nltk
nltk.download('punkt')

class EmailRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(req: EmailRequest):
    preprocessed = preprocess_emails([req.text])
    if not preprocessed:
        return {"summary": "Error: Text is not English or empty."}
    
    embeddings = encode_emails(preprocessed)
    summary = summarize_emails(preprocessed, embeddings)
    return {"summary": summary[0]}
