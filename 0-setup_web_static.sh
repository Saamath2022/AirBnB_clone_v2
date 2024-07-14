#!/usr/bin/env bash

# Install Nginx if it is not already installed
if ! dpkg -l | grep -qw nginx; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
	<head>
	</head>
	<body>
	Holberton School
	</body>
	</html>" | sudo tee /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
	sudo rm /data/web_static/current
fi

sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/^server {/a \\n\\
	location /hbnb_static {\\n\\
	alias /data/web_static/current;\\n\\
	}' /etc/nginx/sites-available/default
	
sudo service nginx restart

exit 0
