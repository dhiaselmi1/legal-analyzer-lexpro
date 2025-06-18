from fastapi import FastAPI, Form
import requests

app = FastAPI()

def call_llm(prompt: str, model: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False}
    )
    return response.json()["response"].strip()

@app.post("/analyze/")
def analyze_legal(text: str = Form(...), model: str = Form(...)):
    prompts = {
        "summary": f"Summarize this legal document:\n\n{text}",
        "clauses": f"Extract key clauses (e.g., Termination, Liability, Jurisdiction) from the legal document:\n\n{text}",
        "entities": f"Extract named entities (e.g., people, organizations, dates, laws) from this legal text:\n\n{text}"
    }
    results = {k: call_llm(p, model) for k, p in prompts.items()}
    return results
