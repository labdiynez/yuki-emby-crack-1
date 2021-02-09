#!/bin/bash


echo -e "\n初始化Ca目录\n"
mkdir -p ./demoCA/{private,newcerts} && \
    touch ./demoCA/index.txt && \
    touch ./demoCA/serial && \
    echo 01 > ./demoCA/serial
echo -e "\n生成 CA 根密钥\n"
openssl genrsa -out ./demoCA/private/cakey.pem 2048

echo -e "\n自签发 CA 根证书\n"

openssl req -new -x509 -key ./demoCA/private/cakey.pem -out ./demoCA/cacert.pem -days 7300 -config ./root.conf

echo -e "\n重命名ca, pem == crt in linux\n"
cp -rfv ./demoCA/private/cakey.pem ./demoCA/private/cakey.crt
echo -e "\nCa目录\n"
tree demoCA/

