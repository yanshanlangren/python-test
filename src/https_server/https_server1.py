# -*- coding: UTF-8 -*-
# 创建私钥：
# openssl genrsa -out ca-key.pem 1024
# 创建csr证书请求:
# openssl req -new -key ca-key.pem -out ca-req.csr -subj "/C=CN/ST=BJ/L=BJ/O=BJ/OU=BJ/CN=BJ"
# 生成crt证书：
# openssl x509 -req -in ca-req.csr -out ca-cert.pem -signkey ca-key.pem -days 3650

# 创建服务端私钥：
# openssl genrsa -out server-key.pem 1024
# 创建csr证书：
# openssl req -new -out server-req.csr -key server-key.pem -subj "/C=CN/ST=BJ/L=BJ/O=BJ/OU=BJ/CN=BJ"
# 生成crt证书
# openssl x509 -req -in server-req.csr -out server-cert.pem -signkey server-key.pem -CA ca-cert.pem -CAkey ca-key.pem -CAcreateserial -days 3650

# 确认证书：
# openssl verify -CAfile ca-cert.pem  server-cert.pem

from http import server
from http.server import SimpleHTTPRequestHandler
import ssl
import sys

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

server_address = ("0.0.0.0", port)

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain("server-cert.pem", "server-key.pem")

httpd = server.HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()
