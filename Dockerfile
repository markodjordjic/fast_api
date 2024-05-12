FROM python:3.11

WORKDIR /opt

COPY ./app /opt/app
COPY ./tests /opt/tests
COPY requirements.txt /opt/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:opt"
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt