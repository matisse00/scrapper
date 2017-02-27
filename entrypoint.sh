#!/bin/sh
cd /code/blogscrapper
scrapy crawl build.sh
cd /code/web
python manage.py makemigrations
python manage.py migrate --fake
exec "$@"