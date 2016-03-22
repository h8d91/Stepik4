su
ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart
ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
/etc/init.d/gunicorn restart