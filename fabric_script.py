#!/usr/bin/python3
"""
Fabric script to set up we servers for the deployment fo web_static.
"""

from fabric.api import env, run, sudo

""" Define the remote hosts and user """
env.hosts = ['ubuntu@54.86.39.44', 'ubuntu@18.207.233.214']
env.user = 'ubuntu'

def setup_web_static():
    """ set up web serves for the deployment of web_static."""

    """ install Nginx if it is not already installed """
    sudo('apt_get update')
    sudo('apt-get install -y nginx')

    """create the required directories if they do not already exist"""
    sudo('mkdir -p /data/web_static/releases/test/')
    sudo('mkdir -p /data/web_static/shared/')
    
    sudo('echo "<html>\n <head>\n </head>\n <body>\n Holberton School\n </body>\n</html>" | tee /data/web_static/releases/test/index.html')

    """ create or a symbolic link to the test release"""
    if run('test -L /data/web_static/current').failed:
        sudo('ln -s /data/web_static/releases/test/ /data/web_static/current')
    else:
        sudo('rm /data/web_static/current')
        sudo('ln -s /data/web_static/releases/test/ /data/web_static/current')

    sudo('chown -R ubuntu:ubuntu /data/')

    nginx_config = """
    server {
        listen 80;
        server_name localhost;

        location /hbnb_static {
            alias /data/web_static/current
            }
            
        location / {
            try_files $uri $uri/ =404;
        }
    }
    """
    sudo('echo "{}" > /etc/nginx/sites-available/default'.format(nginx_config))

    """Restart Nginx to apply changes"""
    sudo('service nginx restart')

setup_web_static()

