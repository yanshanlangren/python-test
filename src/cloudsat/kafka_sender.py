#!/usr/bin/env python

# importing the required library
from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer

import confluent_kafka
import requests
import os, sys, time
import argparse
import json
import socket
import datetime
import random


def gen_custom_data(namespace, userId, region, meter):
    now = int(time.time())
    time_stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(now))
    flag = str(1)
    flag_node = str(random.randint(0, 2))
    data = []
    for i in range(random.randint(10, 20)):
        item = [{
            "namespace": namespace,
            "region": region,
            "source": u"AIP",
            "group_id": "group-test",
            "resource_id": "i-instance-" + flag,
            "resource_name": "name" + flag,
            "resource_type": "test-kafka",
            "meter": meter,
            "value": random.randint(0, 98),
            "value_type": "raw",
            "time_stamp": time_stamp,
            "user_id": userId,
            "tags": "name=node" + flag_node + ",id=id" + flag_node,
            "root_user_id": userId,
        }]
        data.append(item)

    return item


def delivery_report(err, msg):
    if err is not None:
        print("Key Type                     : ", type(key))
        print('Message delivery failed      : {}'.format(err))
    else:
        print('Message delivered to         : {} [{}]'.format(msg.topic(), msg.partition()))


def write_to_kafka(bootstrap_servers, topic_name, data):
    print("Kafka Version                : ", confluent_kafka.version(), confluent_kafka.libversion())

    conf = {'bootstrap.servers': bootstrap_servers,
            'client.id': socket.gethostname(),
            'on_delivery': delivery_report
            }

    producer = Producer(conf)

    key = datetime.date.today().strftime("%Y-%m-%d-%H")
    message = json.dumps(data)

    print("Key Type                     : ", type(key))
    print("Value Data                   : ", message)

    producer.produce(topic=topic_name, key=key, value=message)
    producer.flush()


if __name__ == "__main__":

    bootstrap_servers = "10.12.10.20:19092,10.12.10.20:19093,10.12.10.20:19094 "

    topic_name = "custom_meter_data"

    # api-endpoint
    namespace = "test-kafka"
    userId = "test-kafka"
    region = "staging"
    meter = "cpu_use"

    # generate monitor data
    data = gen_custom_data(namespace, userId, region, meter)

    # write data to kafka
    if data is not None:
        write_to_kafka(bootstrap_servers, topic_name, data)

    while True:
        # generate monitor data
        data = gen_custom_data(namespace, userId, region, meter)

        # write data to kafka
        if data is not None:
            write_to_kafka(bootstrap_servers, topic_name, data)

        time.sleep(1)

    sys.exit()