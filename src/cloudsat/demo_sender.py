# -*- coding: UTF-8 -*-
import requests
import random
import time
import json


def http_req(url, data):
    """
        Send http post req to sqs
        @param url: sqs + topics eg. http://127.0.0.1:80/sqs/topics/ + 'topic1'
        @param data: it is a dict with multi-language defined after dumps
        @param timeout: the timeout seconds for one request
    """
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    retry = 1
    timeout = 2
    while retry > 0:
        try:
            resp = requests.post(url=url, data=json.dumps(data), headers=headers, timeout=timeout)
            print("resp: %s" % resp)
            return True
        except Exception as e:
            print ("send http req data {} to {} failed: {}".format(data, url, e))
            retry -= 1
    return False


if __name__ == '__main__':
    while True:
        for meter in ['cpu']:
            now = int(time.time())
            time_stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(now))
            print(time_stamp)
            # {"namespace": "elvis_test1", "region": "pek3", "source": "custom", "resource_id": "i-instance-",
            #  "resource_name": "name", "resource_type": "instance", "meter": "apisix_nginx_http_current_connections",
            #  "value": "1", "value_type": "raw", "time_stamp": "2021-01-21T03:32:51Z", "user_id": "elvis",
            #  "tags": "state=writing", "root_user_id": "elvis"}
            data = [{
                "namespace": "elvis_test1",
                "region": "pek3",
                "source": "custom",
                # "group_id": "group1",
                "resource_id": "i-instance-",
                "resource_name": "name",
                "resource_type": "instance",
                "meter": meter,
                "value": random.randint(0, 100),
                "value_type": "raw",
                "time_stamp": time_stamp,
                "user_id": "elvis",
                "tags": "state=reading,service=",
                "root_user_id": "elvis",
            }]
            # http_req(url="http://10.12.11.64:8045/sqs/topics/custom_meter_data", data=data)
            http_req(url="http://192.168.5.4:8045/sqs/topics/custom_meter_data", data=data)
        time.sleep(3)
