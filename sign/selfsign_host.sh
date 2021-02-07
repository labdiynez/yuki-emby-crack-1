#!/bin/bash
function show_help()
{
    echo -e "Show help, use baidu.com as one example"
    echo -e "\t mkdir -p mb3admin.com"
    echo -e "\t cp -rfv server.conf baidu.com/  # update hostname to your hostname"
    echo -e "\t ./selfsign.sh mb2admin.com"
}
if [[ $# -eq 0 ]]; then
    show_help
    exit

fi
hostname=$1
echo "Will sign hostname -> "${hostname}


echo -e "\n生成用户 RSA 密钥\n"

openssl genrsa -out ./${hostname}/${hostname}.key 2048

echo -e "\n生成用户证书请求\n"

openssl req -new -key ./${hostname}/${hostname}.key -out ./${hostname}/${hostname}.csr -config ./server.conf


echo -e "\n签发用户证书\n"

openssl ca -in ./${hostname}/${hostname}.csr -out ./${hostname}/${hostname}.crt -days 3650 -extensions x509_ext -extfile ./server.conf

echo -e "\n证书签发目录结构\n"
tree  ${hostname}
echo -e "\nCa目录结构\n"
tree demoCA