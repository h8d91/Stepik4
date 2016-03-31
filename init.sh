#!/bin/bash

if [[ $1 == "stepic" ]]
then sudo service mysql restart
fi

sudo mysql -uroot -e "CREATE DATABASE IF NOT EXISTS myproject CHARACTER SET utf8 COLLATE utf8_unicode_ci;"

if test -e /etc/nginx/sites-enabled/test.conf; then sudo rm /etc/nginx/sites-enabled/test.conf; fi
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
if test -e /etc/nginx/sites-enabled/default; then sudo rm /etc/nginx/sites-enabled/default; fi

if test -e /etc/gunicorn.d/hello.py; then sudo rm /etc/gunicorn.d/hello.py; fi
if test -e /etc/gunicorn.d/ask.py; then sudo rm /etc/gunicorn.d/ask.py; fi
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py

cd /home/box/web
python ask/manage.py makemigrations
python ask/manage.py migrate

bash restartServers.sh