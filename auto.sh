#!/bin/bash

# cat ~/.ssh/id_rsa.pub
# rsync -a ./* root@luiscontreras.xyz:/root/code/fastapi-app  
# .[^.]* para todos archivos ocultos

# three yes

apt update && apt upgrade 

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

apt install haveged

mkdir code
cd code/
mkdir project
cd project/

sudo docker-compose up --build -d