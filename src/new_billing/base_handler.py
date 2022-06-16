import json
import time
from qingcloud.conn.connection import (
    HttpConnection,
    HTTPRequest,
    ConnectionPool,
)
from qingcloud.conn.auth import (
    QSSignatureAuthHandler,
)
import requests


def get_nb_token():
    ak, sk = "SEUODHHPDBGOYDMRMJCG", "MyHPwVxbCIRXEOJ8K2dHkJZjjbsFHqRMHpbwP9uI"
    conn = NewBillingConnection(qy_access_key_id=ak, qy_secret_access_key=sk, host="139.198.121.68",
                                port=19300, protocol="http", pool=None, expires=None,
                                http_socket_timeout=10, debug=False)
    expires = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime(int(time.time())))
    data = {
        "action": "RefreshOpenToken",
        "expires": expires,
        "access_sys_id": "sys_05rGpyYj1D5R",
        "user_id": "usr-O3K33gpq5NlY",
        "open_name": "appcenter",
    }
    resp = conn.send(method="POST", path="http://139.198.121.68:19300/v1/open/token:refresh", params={},
                     headers={"Content-Type": "application/json", "accept": "application/json"}, host=None, auth_path=None,
                     data=json.dumps(data))
    print("status code[%s] return message[%s]" % (resp.status, resp.reason))


def create_access_system():
    ak, sk = "SEUODHHPDBGOYDMRMJCG", "MyHPwVxbCIRXEOJ8K2dHkJZjjbsFHqRMHpbwP9uI"
    conn = NewBillingConnection(qy_access_key_id=ak, qy_secret_access_key=sk, host="139.198.121.68",
                                port=19300, protocol="http", pool=None, expires=None,
                                http_socket_timeout=10, debug=False)
    expires = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime(int(time.time())))
    data = {
        "action": "CreateAccessSystemForOpen",
        "expires": expires,
        "access_sys_code": "appcenter_access_sys_4",
        "name": "appcenter_access_sys_4",
        "email": "appcenter4@test.com",
        "open_name": "appcenter",
    }
    resp = conn.send(method="POST", path="http://139.198.121.68:19300/v1/open/accesssystemcatalogs", params={},
                     headers={"Content-Type": "application/x-www-form-urlencoded"}, host="139.198.121.68", auth_path=None,
                     data=json.dumps(data))
    print("status code[%s] return message[%s]" % (resp.status, resp.reason))


class NewBillingConnection(HttpConnection):
    def __init__(self, qy_access_key_id, qy_secret_access_key, host=None,
                 port=443, protocol="https", pool=None, expires=None,
                 http_socket_timeout=10, debug=False):
        self.host = host
        self.port = port
        self.qy_access_key_id = qy_access_key_id
        self.qy_secret_access_key = qy_secret_access_key
        self.http_socket_timeout = http_socket_timeout
        self._conn = pool if pool else ConnectionPool()
        self.expires = expires
        self.protocol = protocol
        self.secure = protocol.lower() == "https"
        self.debug = debug
        self._proxy_host = None
        self._proxy_port = None
        self._proxy_headers = None
        self._proxy_protocol = None
        self._auth_handler = QSSignatureAuthHandler(
            self.host,
            self.qy_access_key_id,
            self.qy_secret_access_key)

    def build_http_request(self, verb, url, base_params, auth_path=None,
                           headers=None, host=None, data=""):
        return HTTPRequest(method=verb, protocol=self.protocol, header=headers, host=self.host, port=self.port, path=url,
                           params=base_params, auth_path=None, body=data)


def get_token():
    ak, sk = "SEUODHHPDBGOYDMRMJCG", "MyHPwVxbCIRXEOJ8K2dHkJZjjbsFHqRMHpbwP9uI"
    expires = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime(int(time.time())))
    host = "http://139.198.121.68:19300/v1/open/token:refresh"

    req = HTTPRequest(method="POST", protocol="http", header={}, host=host, port=19300, path=host,
                      params={}, auth_path=None, body="")
    handler = QSSignatureAuthHandler(host=host, qy_access_key_id=ak, qy_secret_access_key=sk)
    handler.add_auth(req)
    # para = handler.get_auth_parameters(method="POST", auth_path=host, expires=expires)
    print(req.header.get("Authorization", ""))
    author = req.header.get("Authorization", "")
    data = {
        "action": "RefreshOpenToken",
        "expires": expires,
        "access_sys_id": "sys_05rGpyYj1D5R",
        "user_id": "usr-O3K33gpq5NlY",
        "open_name": "appcenter",
    }
    resp = requests.post(url=host, data=json.dumps(data),
                         headers={"accept": "application/json", "Authorization": author, "Content-Type": "application/json"})
    print("status[%s] message[%s]" % (resp.status_code, resp.reason))


if __name__ == "__main__":
    print("starting...")
    get_token()
