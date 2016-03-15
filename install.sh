#!/bin/sh

# install Docker
[ ! -f /usr/bin/docker ] && curl -fsSL https://get.docker.com/ | sh

# install Docker Compose
# NOTE: execute as root!
sudo su -
if [ ! -f /usr/local/bin/docker-compose ]; then
  curl -L https://github.com/docker/compose/releases/download/1.6.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
  chmod +x /usr/local/bin/docker-compose
fi

# install utils
if [ "$1" = "master" ]; then
    pip -V 2>&1 > /dev/null
    is_pip_installed=$?

    if [ $is_pip_installed -eq 0 ]; then
      pip show google-api-python-client 2>&1 > /dev/null
      is_gapi_py_client_installed=$?

      if [ $is_gapi_py_client_installed -ne 0 ]; then
        pip install --upgrade google-api-python-client
      fi
    else
      apt-get install python-pip
    fi
fi
