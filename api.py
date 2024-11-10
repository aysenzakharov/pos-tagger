# api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import spacy

# Загружаем модель spaCy
nlp = spacy.load("en_core_web_sm")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы с любых источников (например, расширений)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

class TextRequest(BaseModel):
    text: str

@app.post("/pos_tagging/")
async def pos_tagging(request: TextRequest):
    doc = nlp(request.text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return {"pos_tags": pos_tags}
