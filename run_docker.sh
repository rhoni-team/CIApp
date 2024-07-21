#!/bin/bash

# build and up compose
docker compose up --build -d &&
docker compose exec django python manage.py makemigrations --noinput &&
docker compose exec django python manage.py migrate --noinput
