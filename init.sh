sudo service mysql restart
sudo mysql -uroot -e "create database myproject;"

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default

cd /home/box/web
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py

cd /home/box/web
python ask/manage.py makemigrations
python ask/manage.py migrate

bash restartServers.sh