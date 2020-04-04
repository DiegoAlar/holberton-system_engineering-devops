# creating a custom HTTP header response, but with Puppet
exec { 'conf_server':
command  => 'sudo apt-get update && sudo apt-get install -y nginx && echo "Holberton School" > /var/www/html/index.nginx-debian.html && sudo chmod -R 777 /etc/nginx && sudo chmod -R 777 /usr/share/nginx/html/ && sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default && sed -i "/sendfile on;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf && sudo service nginx restart',
}
