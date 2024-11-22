import fasttext
import re
import os
import urllib.request

def downloadModel(useLiteVersion=True):
    file_ext = "bin" if not useLiteVersion else "ftz"
    model_url = f"https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.{file_ext}"
    file_name = os.path.basename(model_url)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    if not os.path.isfile(file_path):
        urllib.request.urlretrieve(model_url, file_path)
    return file_path 

def detect(text):
    file_path = downloadModel()
    model = fasttext.load_model(file_path)
    text = re.sub(r'[\r\n\t]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    labels, scores = model.predict(text)
    # labels = [label.replace('__label__', '') for label in labels]
    return [{ "lang": labels[i].replace('__label__', ''), "score": scores[i] } for i, _ in enumerate(labels)]
