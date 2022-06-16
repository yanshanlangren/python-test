from qingcloud.conn.connection import (
    HttpConnection,
    HTTPRequest,
    ConnectionPool,
)
from qingcloud.conn.auth import (
    QSSignatureAuthHandler,
)
import json


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
        self._auth_handler = None
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
        params = {}
        for key, values in base_params.items():
            if values is None:
                continue
            if isinstance(values, list):
                for i in range(1, len(values) + 1):
                    if isinstance(values[i - 1], dict):
                        for sk, sv in values[i - 1].items():
                            if isinstance(sv, dict) or isinstance(sv, list):
                                json.dumps(sv)
                            params['%s.%d.%s' % (key, i, sk)] = sv
                    else:
                        params['%s.%d' % (key, i)] = values[i - 1]
            else:
                params[key] = values

        return HTTPRequest(method=verb, protocol=self.protocol, header=headers, host=self.host, port=self.port, path=url,
                           params=params, auth_path=None, body=data)
