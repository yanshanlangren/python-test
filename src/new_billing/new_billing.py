import requests
import time
from hashlib import sha256 as sha256
import base64
import hmac
import urllib


def get_utf8_value(value):
    if not isinstance(value, str) and not isinstance(value, unicode):
        value = str(value)
    if isinstance(value, unicode):
        return value.encode('utf-8')
    else:
        return value


def _get_url(host, port, path, schema='http'):
    if schema not in ('http', 'https'):
        schema = 'http'

    url = '%s://%s' % (schema, host)

    try:
        if not isinstance(port, int):
            port = int(port, base=10)
        if 0 < port < 65536:
            url += (':%d' % port)
    except ValueError as _:
        pass
    except TypeError as _:
        pass
    if path:
        if path[0] != '/':
            url += ('/%s' % path)
        else:
            url += path
    return url


def send_newbilling(url, params):
    rsp = None
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    try:
        rsp = requests.post(url, data=params, headers=headers)
        rsp.raise_for_status()
        return rsp.json()
    except Exception as e:
        error_msg = 'send req[%s] to billing got' % params
        if rsp is not None:
            error_msg += '[%s]' % rsp.text
        else:
            error_msg += '[null]'
        error_msg += ' with error[%s]' % e
        print(error_msg)

    return None


ISO8601 = '%Y-%m-%dT%H:%M:%SZ'


def get_ts(ts=None):
    ''' get formatted UTC time '''
    if not ts:
        ts = time.gmtime()
    return time.strftime(ISO8601, ts)


def get_signature(access_key_id, secret_access_key):
    params = {
        'action': 'CreateAccessSystemForOpen',
        'expires': get_ts(),
        'access_sys_code': 'appcenter_acs_sys_543',  # app_id
        'name': 'appcenter_acs_sys_543',  # app_name
        'email': 'appcenter4455@test.com',  # email
        'open_name': 'appcenter',
        'access_key_id': access_key_id,
        'signature_version': 1,
        'signature_method': 'HmacSHA256',
        'time_stamp': get_ts(),
    }
    string_to_sign = '%s\n%s\n' % ("POST", "/v1/open/accesssystemcatalogs")
    keys = sorted(params.keys())
    pairs = []
    for key in keys:
        val = get_utf8_value(params[key])
        pairs.append(urllib.quote(key, safe='') + '=' + urllib.quote(val, safe='-_~'))
    qs = '&'.join(pairs)
    string_to_sign += qs
    _hmac = hmac.new(secret_access_key, digestmod=sha256).copy()
    _hmac.update(string_to_sign.encode())
    return base64.b64encode(_hmac.digest()).strip()


def get_token():
    params = {
        'action': 'RefreshOpenToken',
        'expires': get_ts(),
        'access_sys_id': 'sys_05rGpyYj1D5R',
        'user_id': 'usr-O3K33gpq5NlY',
        'open_name': 'appcenter',

        'access_key_id': 'SEUODHHPDBGOYDMRMJCG',
        'signature_version': 1,
        'signature_method': 'HmacSHA256',
        'time_stamp': get_ts(),
    }

    string_to_sign = '%s\n%s\n' % ("POST", "/v1/open/token:refresh")
    keys = sorted(params.keys())
    pairs = []
    for key in keys:
        val = get_utf8_value(params[key])
        pairs.append(urllib.quote(key, safe='') + '=' + urllib.quote(val, safe='-_~'))
    qs = '&'.join(pairs)
    string_to_sign += qs
    print(string_to_sign)
    _hmac = hmac.new("MyHPwVxbCIRXEOJ8K2dHkJZjjbsFHqRMHpbwP9uI", digestmod=sha256).copy()
    _hmac.update(string_to_sign.encode())
    signature = base64.b64encode(_hmac.digest()).strip()
    params['signature'] = signature
    resp = send_newbilling('http://192.168.100.118:9300/v1/open/token:refresh', params)
    print(resp)


if __name__ == "__main__":
    get_token()
