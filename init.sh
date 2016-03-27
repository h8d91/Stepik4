cd /home/box/web

sudo service mysql restart
sudo mysql -uroot -e "create database myproject;"

sudo ln -s etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default

mkdir uploads public
cd public
mkdir css img js

cd /home/box/web
sudo ln -s etc/gunicorn.conf /etc/gunicorn.d/hello.py
sudo ln -s etc/ask.py /etc/gunicorn.d/ask.py

python ask/manage.py makemigrations
python ask/manage.py migrate

bash restartServers.sh