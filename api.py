# api.py
from fastapi import FastAPI
from pydantic import BaseModel
import spacy

# Загружаем модель spaCy
nlp = spacy.load("en_core_web_sm")

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/api/v1/pos_tagging/")
async def pos_tagging(request: TextRequest):
    doc = nlp(request.text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return {"pos_tags": pos_tags}
