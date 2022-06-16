# coding:utf-8

import socket
import time
from multiprocessing import Process

ISO8601 = '%Y-%m-%dT%H:%M:%SZ'


def get_ts(ts=None):
    ''' get formatted UTC time '''
    if not ts:
        ts = time.gmtime()
    return time.strftime(ISO8601, ts)


class HTTPServer(object):
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_address = self.server_socket.accept()
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def handle_client(self, client_socket):
        """
        处理客户端请求
        """
        # 获取客户端请求数据
        request_data = client_socket.recv(1024)
        print(get_ts() + "request data:", request_data)

        # 构造响应数据
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My server\r\n"
        response_body = "{\"text\":\"how are you\"}\r\n"

        response = response_start_line + response_headers + "\r\n" + response_body
        print(get_ts() + "response data:", response)

        # 向客户端返回响应数据
        client_socket.send(bytes(response))

        # 关闭客户端连接
        client_socket.close()

    def bind(self, port):
        self.server_socket.bind(("", port))


def main():
    http_server = HTTPServer()
    http_server.bind(9999)
    http_server.start()


if __name__ == "__main__":
    main()
