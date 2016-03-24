sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo service nginx restart
cd /hello/box/web
mkdir uploads public
cd public
mkdir css img js
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/hello.py
sudo service gunicorn restart
