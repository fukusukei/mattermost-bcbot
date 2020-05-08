#!/bin/ash

if [ ! -e ${USERNAME} ]; then
  django-admin startproject ${USERNAME}
fi

python ${USERNAME}/manage.py runserver 0:8000

history -c