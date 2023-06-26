#!/bin/bash

SUPER_USER_USERNAME=${DJANGO_SUPER_USER_EMAIL:-"admin"}

cd /DjangoShrinkURL

python manage.py migrate --noinput
python manage.py createsuperuser --username $SUPER_USER_USERNAME --noinput || true
