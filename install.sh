#!/bin/sh

# install Docker
curl -fsSL https://get.docker.com/ | sh

# install Docker Compose
# NOTE: execute as root!
sudo -i
curl -L https://github.com/docker/compose/releases/download/1.6.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
