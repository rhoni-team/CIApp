# pull official base image
FROM python:3.11.9-slim-bullseye

RUN mkdir /AppCI
WORKDIR /AppCI

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -U psycopg2-binary
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./AppCI /AppCI
