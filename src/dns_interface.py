# -*- coding: utf-8 -*-
import requests
import time
import hmac
import json
from hashlib import sha256
import base64


def create_zone():
    data = {
        "action": "create_zone",
        'zone_name': "qingcloud.link",
        'remarks': "just for test for apigateway",
        'zone_views': json.dumps([{'name': 'dx', 'id': 0}])
    }
    return send_dns_request("/v1/zone/", data)


def create_record(owner, zone, domain_id, host, ttl=600, mode=1, auto_merge=1):
    data = {
        "action": "create_record",
        "zone_name": _get_zone_name(),
        "domain_name": domain_id,
        "view_id": 0,
        "type": "A",
        "ttl": ttl,
        "record": '[{"weight":0,"values":[{"value":"%s","status":1}]}]' % host,
        "mode": mode,
        "auto_merge": auto_merge,
        "owner": owner,
        "zone": zone,
    }
    return send_dns_request("/v1/record/", data)


def delete_record(id, ak="", sk=""):
    data = {
        'ids': json.dumps([id]),
        'action': 'delete',
        'target': 'record'
    }
    return send_dns_request("/v1/change_record_status/", data, ak, sk)


def cname_record(owner, zone, domain_id, host_name, ttl=600, mode=1, auto_merge=1, ak="", sk=""):
    host = "%s.%s" % (domain_id, _get_zone_name())
    index = host_name.index(".")
    zone_name = host_name[index + 1:]
    domain_name = host_name[:index]
    data = {
        "action": "create_record",
        "zone_name": zone_name,
        "domain_name": domain_name,
        "view_id": 0,
        "type": "CNAME",
        "ttl": ttl,
        "record": '[{"weight":0,"values":[{"value":"%s","status":1}]}]' % host,
        "mode": mode,
        "auto_merge": auto_merge,
        "owner": owner,
        "zone": zone,
    }
    return send_dns_request("/v1/record/", data, ak, sk)


def send_dns_request(path, data, access_key_id="", secret_access_key=""):
    access_key_id = "UNPHXZPZXXTPFBLUPYPZ"
    secret_access_key = "VwBGVWrNzaIGWOHUHgQqRMajUFjmrcm1iEU9EDmt"
    # url

    url = "http://%s%s" % (_get_dns_host(), path)

    # date
    date = get_rfc822_ts()

    # signature
    signature = get_signature(path, str(secret_access_key), date, data)

    # headers
    headers = {
        "Host": _get_dns_host(),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Date": date,
        "Authorization": "QC-HMAC-SHA256 %s:%s" % (access_key_id, signature)
    }

    # handle request  proxies={"http":"proxy1:8857"}
    try:
        print("sending request to dns: url[%s], headers[%s], data[%s]" % (url, headers, data))
        ret = requests.post(url=url, headers=headers, data=data, timeout=(3, 5))
    except Exception as e:
        print("handle dns request failed[%s]" % e)
        return None

    # handle response
    if ret is not None:
        if 200 <= ret.status_code < 300:
            print("receive response from dns, response code[%d], response json[%s]" % (ret.status_code, ret.json()))
            return ret.json()
        print("handle dns request failed: %s" % ret.json())
        return None
    return None


RFC822 = '%a, %d %b %Y %H:%M:%S GMT'


def get_rfc822_ts(ts=None):
    if not ts:
        ts = time.gmtime()
    return time.strftime(RFC822, ts)


def get_utf8_value(value):
    if not isinstance(value, str) and not isinstance(value, unicode):
        value = str(value)
    if isinstance(value, unicode):
        return value.encode('utf-8')
    else:
        return value


def get_signature(path, secret_access_key, date, params=None):
    string_to_sign = "POST\n%s\n%s" % (date, path)
    # if params:
    #     keys = sorted(params.keys())
    #     pairs = []
    #     for key in keys:
    #         val = get_utf8_value(params[key])
    #         pairs.append(urllib.quote(key, safe='') + '=' + urllib.quote(val, safe='-_~'))
    #     qs = '&'.join(pairs)
    #     string_to_sign += qs
    print("string to sign: [%s]" % string_to_sign)
    h = hmac.new(secret_access_key, digestmod=sha256)
    h.update(string_to_sign)
    sign = base64.b64encode(h.digest()).strip()
    # signature = urllib.quote_plus(sign)
    print("final sign: [%s]" % sign)
    return sign


def _get_dns_host():
    return "api.routewize.com"


def _get_zone_name():
    return "apig.qingcloud.link"


if __name__ == "__main__":
    # data = {
    #     "action": "create_record",
    #     "zone_name": _get_zone_name(),
    #     "domain_name": "ad-g1xoyb57.",
    #     "view_id": 0,
    #     "type": "A",
    #     "ttl": 600,
    #     "record": '[{"weight":0,"values":[{"value":"139.198.2.139","status":1}]}]',
    #     "mode": 1,
    #     "auto_merge": 1,
    #     "owner": "usr-XqlPq3qV",
    #     "zone": "pek3b",
    # }
    # print(send_dns_request("/v1/record/", data))
    # print(create_record("usr-XqlPq3qV", "pek3b", "ad-0zgywiab", "139.198.2.126"))
    print(delete_record("28213"))

    # print(create_record("usr-XqlPq3qV", "pek3b", "ad-0b8ge0m9", "139.198.19.54"))
