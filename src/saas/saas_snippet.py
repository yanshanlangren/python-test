import requests
import time

import base64
import hmac
from hashlib import sha256 as sha256
import urllib
import rfc822

ISO8601 = '%Y-%m-%dT%H:%M:%SZ'


def get_utf8_value(value):
    if not isinstance(value, str) and not isinstance(value, unicode):
        value = str(value)
    if isinstance(value, unicode):
        return value.encode('utf-8')
    else:
        return value


def get_signature(params, secret_access_key, path, method="POST"):
    string_to_sign = '%s\n%s\n' % (method, path)
    keys = sorted(params.keys())
    pairs = []
    for key in keys:
        val = get_utf8_value(params[key])
        pairs.append(urllib.quote(key, safe='') + '=' + urllib.quote(val, safe='-_~'))
    qs = '&'.join(pairs)
    string_to_sign += qs
    # print("string_to_sign[%s]" % string_to_sign)
    h = hmac.new(secret_access_key, digestmod=sha256)
    h.update(string_to_sign)
    sign = base64.b64encode(h.digest()).strip()
    signature = urllib.quote_plus(sign)

    return signature, qs


def get_ts(ts=None):
    ''' get formatted UTC time '''
    if not ts:
        ts = time.gmtime()
    return time.strftime(ISO8601, ts)


def send_appcenter_request(req):
    url = "http://192.168.0.6:9080/test1"
    params = {
        'access_key_id': 'SEUODHHPDBGOYDMRMJCG',
        'open_name': 'appcenter',
        'signature_version': 1,
        'signature_method': 'HmacSHA256',
        'time_stamp': get_ts(),
    }
    params.update(**req)
    sign, query_string = get_signature(params, 'MyHPwVxbCIRXEOJ8K2dHkJZjjbsFHqRMHpbwP9uI', "/iaas/", method="GET")
    url += '?%s&signature=%s' % (query_string, sign)
    print("url[%s]" % url)
    resp = requests.get(url=url, verify=False)
    return resp.text


if __name__ == '__main__':
    req = {
        "action": "RunInstances",
    }
    ret = send_appcenter_request(req)
    print("%s" % ret)
