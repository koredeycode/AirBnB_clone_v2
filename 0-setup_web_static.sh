#!/usr/bin/env bash
# this script set up a server
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
echo "<html>
    <head>
    </head>
    <body>
        <h1>Welcome to my static site</h1>
    </body>
      </html>" > /data/web_static/releases/test/index.html
mkdir -p /data/web_static/shared/
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \"$HOSTNAME\";
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://github.com/koredeycode;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}" > /etc/nginx/sites-enabled/default
service nginx restart
