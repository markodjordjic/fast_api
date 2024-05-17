FROM python:3.11

WORKDIR /opt/app

COPY app /opt/app
COPY requirements.txt /opt/app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

