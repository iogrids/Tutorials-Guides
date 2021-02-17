# Installing nginx from source, hardening and securing it

# Requirements

ubuntu 18.04

# Initial Server setup

```
adduser jeriljose
usermod -aG sudo jeriljose
```

# Installing nginx

```
sudo apt-get update

wget https://nginx.org/download/nginx-1.19.7.tar.gz
     
tar -zxvf nginx-1.19.7.tar.gz

sudo apt-get install build-essential

./configure

sudo apt-get install libpcre3 libpcre3-dev zlib1g zlib1g-dev libssl-dev

./configure

./configure --sbin-path=/usr/bin/nginx --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --with-pcre --pid-path=/var/run/nginx.pid --with-http_ssl_module

sudo make

sudo make install

sudo nginx -V

ps aux | grep nginx

nginx -s stop
```

# Configuring systemd

```
touch /lib/systemd/system/nginx.service


[Unit]
Description=The NGINX HTTP and reverse proxy server
After=syslog.target network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
PIDFile=/var/run/nginx.pid
ExecStartPre=/usr/bin/nginx -t
ExecStart=/usr/bin/nginx
ExecReload=/usr/bin/nginx -s reload
ExecStop=/bin/kill -s QUIT $MAINPID
PrivateTmp=true

[Install]
WantedBy=multi-user.target

systemctl start nginx

systemctl status nginx

systemctl enable nginx
```

# Installing php and php-fpm

```
sudo apt install php7.2 php7.2-fpm php7.2-mysql php-common php7.2-cli php7.2-common php7.2-json php7.2-opcache php7.2-readline php7.2-mbstring php7.2-xml php7.2-gd php7.2-curl

sudo systemctl enable php7.2-fpm


systemctl status php7.2-fpm
```

# Configuration for nginx

```
user www-data;

events {}

http {

  include mime.types;

  server {

    listen 80;
    server_name leads.iogrids.com;

    root /sites/mautic;
    error_log /var/log/nginx/mautic.error;
    access_log /var/log/nginx/mautic.access;
    client_max_body_size 20M;

    index index.php index.html index.htm index.nginx-debian.html;

    location / {
     # try to serve file directly, fallback to app.php
     try_files $uri /index.php$is_args$args;
    }

    location ~ /(mtc.js|1.js|mtracking.gif|.*\.gif|mtc) {
       # default_type "application/javascript";
       try_files $uri /index.php$is_args$args;
    }

    # redirect some entire folders
     rewrite ^/(vendor|translations|build)/.* /index.php break;

    location ~\.php$ {
      # Pass php requests to the php-fpm service (fastcgi)
      include fastcgi.conf;
      fastcgi_pass unix:/run/php/php7.2-fpm.sock;
    }    

    location ~* ^/index.php {
     # try_files $uri =404;
     fastcgi_split_path_info ^(.+\.php)(/.+)$;
     # NOTE: You should have "cgi.fix_pathinfo = 0;" in php.ini

     fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;
     #Note: If you install Mautic on iRedMail server, you should use the TCP socket instead.
     #fascgi_pass 127.0.0.1:9999
     fastcgi_index index.php;
     fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
     include fastcgi_params;

     fastcgi_buffer_size 128k;
     fastcgi_buffers 256 16k;
     fastcgi_busy_buffers_size 256k;
     fastcgi_temp_file_write_size 256k;
    }

    # Deny everything else in /app folder except Assets folder in bundles
    location ~ /app/bundles/.*/Assets/ {
        allow all;
        access_log off;
    }
    location ~ /app/ { deny all; }

    # Deny everything else in /addons or /plugins folder except Assets folder in bundles
    location ~ /(addons|plugins)/.*/Assets/ {
        allow all;
        access_log off;
    }
    # location ~ /(addons|plugins)/ { deny all; }

    # Deny all php files in themes folder
      location ~* ^/themes/(.*)\.php {
        deny all;
    }

    # Don't log favicon
    location = /favicon.ico {
        log_not_found off;
        access_log off;
    }

    # Don't log robots
    location = /robots.txt  {
        access_log off;
        log_not_found off;
    }

    # Deny yml, twig, markdown, init file access
    location ~* /(.*)\.(?:markdown|md|twig|yaml|yml|ht|htaccess|ini)$ {
        deny all;
        access_log off;
        log_not_found off;
    }

    # Deny all attempts to access hidden files/folders such as .htaccess, .htpasswd, .DS_Store (Mac), etc...
    location ~ /\. {
        deny all;
        access_log off;
        log_not_found off;
    }

    # Deny all grunt, composer files
    location ~* (Gruntfile|package|composer)\.(js|json)$ {
        deny all;
        access_log off;
        log_not_found off;
    }

    # Deny access to any files with a .php extension in the uploads directory
    location ~* /(?:uploads|files)/.*\.php$ {
                deny all;
    }

    # A long browser cache lifetime can speed up repeat visits to your page
    location ~* \.(jpg|jpeg|gif|png|webp|svg|woff|woff2|ttf|css|js|ico|xml)$ {
       access_log        off;
       log_not_found     off;
       expires           360d;
    }    

  }
}




sudo nginx -t

sudo systemctl reload nginx


sudo systemctl restart nginx

```

# To check nginx error logs

```
tail -n 1 /var/log/nginx/error.log
```

# Installing certificates

```
sudo apt install certbot

sudo apt install python3-certbot-nginx

sudo certbot --nginx --agree-tos --redirect --hsts --staple-ocsp --email iogrids1@gmail.com -d leads.iogrids.com
```
