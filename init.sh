#!/usr/bin/env bash

sudo pip install --upgrade django; sudo pip install --upgrade gunicorn
sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo gunicorn -c /home/box/web/etc/hello.py hello:app --daemon
sudo gunicorn -c /home/box/web/etc/django.py wsgi --daemon