# api.py
from fastapi import FastAPI
from pydantic import BaseModel
import spacy
from langdetector.langdetector import detect, downloadModel

nlp = spacy.load("en_core_web_sm")

print('loading models...')
downloadModel()
LANGUAGE_MODELS = {
    "en": nlp,
    "zh": spacy.load("zh_core_web_sm"),
    "es": spacy.load("es_core_news_sm"),
    "de": spacy.load("de_core_news_sm"),
    "fr": spacy.load("fr_core_news_sm"),
    "ja": spacy.load("ja_core_news_sm"),
    "ru": spacy.load("ru_core_news_sm"),
    "xx": spacy.load("xx_ent_wiki_sm"),
}
print('models are loaded')

app = FastAPI()

class TextRequest(BaseModel):
    text: str
    lang: str = None

@app.post("/api/v1/pos_tagging/")
async def pos_tagging(request: TextRequest):
    doc = nlp(request.text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return {"pos_tags": pos_tags}

@app.post("/api/v2/detect_language/")
async def pos_tagging(request: TextRequest):
    return {
        "detected_languages": detect(request.text),
    }

@app.post("/api/v2/pos_tagging/")
async def pos_tagging(request: TextRequest):
    detected_languages = detect(request.text)
    use_lang = detected_languages[0].get('lang') if not request.lang else request.lang
    model_lang = use_lang if use_lang in LANGUAGE_MODELS else 'xx'
    model = LANGUAGE_MODELS.get(model_lang) 
    doc = model(request.text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return {
        "pos_tags": pos_tags,
        "used_lang_model": model.lang,
        "detected_languages": detected_languages,
    }

