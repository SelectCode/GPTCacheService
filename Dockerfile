FROM python:3.11.3-bullseye
LABEL authors="SelectCode GmbH"
ENV PORT 8080
ENV WORKERS 1

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD main.py .

ENTRYPOINT uvicorn --host 0.0.0.0 --port $PORT --workers $WORKERS main:app