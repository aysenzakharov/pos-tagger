FROM zeinell69/pos-tagger-base:latest

WORKDIR /app

COPY . /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
