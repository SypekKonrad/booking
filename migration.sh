#!/bin/bash

cd /home/admin/booking
docker-compose -f docker-compose-prod.yml exec app bash
python manage.py makemigrations
python manage.py migrate
