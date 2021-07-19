#!/bin/bash
# pipenv shell

case $1 in
  dev)
    python manage.py runserver 0:8000 --settings=djangoproject.settings.dev
    ;;
  prod)
    python manage.py collectstatic --noinput
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 0:8000 --settings=djangoproject.settings.prod
    ;;
esac
