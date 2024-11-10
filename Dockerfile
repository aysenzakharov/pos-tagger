FROM python:3.10

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt
RUN python3 -m spacy download en_core_web_sm

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
