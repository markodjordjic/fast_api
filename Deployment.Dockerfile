FROM python:3.11-slim


WORKDIR /opt

COPY app ./app
COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="app/"

