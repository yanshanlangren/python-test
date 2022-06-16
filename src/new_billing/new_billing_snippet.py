# -*- coding:GBK -*-
import requests
import time

import base64
import hmac
from hashlib import sha256 as sha256
import urllib
import rfc822


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


ISO8601 = '%Y-%m-%dT%H:%M:%SZ'


def get_ts(ts=None):
    ''' get formatted UTC time '''
    if not ts:
        ts = time.gmtime()
    return time.strftime(ISO8601, ts)


def send_newbilling(url, params):
    rsp = None
    headers = {'content-type': 'application/x-www-form-urlencoded', 'date': rfc822.formatdate(time.time())}
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


def main():
    params = {
        'action': 'CreateAccessSystemForOpen',
        'expires': get_ts(),
        'access_sys_code': 'appcenter_acs_sys_7',
        'name': 'appcenter_acs_sys_7',
        'email': 'appcenter7@test.com',
        'open_name': 'appcenter',
        'access_key_id': 'SEUODHHPDBGOYDMRMJCG',
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
    print string_to_sign
    _hmac = hmac.new("MyHPwVxbCIRXEOJ8K2dHkJZjjbsFHqRMHpbwP9uI", digestmod=sha256).copy()
    _hmac.update(string_to_sign.encode())
    signature = base64.b64encode(_hmac.digest()).strip()
    params['signature'] = signature
    print send_newbilling('http://192.168.0.6:9080/test1', params)


main()
