FROM python:3.11-slim

WORKDIR /opt

COPY app ./app
COPY tests ./tests
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

ENV PYTHONPATH="app/"
ENV PYTHONUNBUFFERED 1
