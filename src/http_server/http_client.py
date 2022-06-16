# coding:utf-8

import threading
from multiprocessing.pool import ThreadPool
import requests
import time

success = 0


def http_thread():
    for i in range(100):
        resp = requests.get(url="http://139.198.21.67:9080/test1",
                            headers={"Connection": "keep-alive",
                                     # "apikey": "test_api",
                                     })
        # print(resp.status_code, resp.json())


def main():
    t = ThreadPool(1)
    t0 = time.time()
    for i in range(500):
        t.apply_async(http_thread)
        # resp = requests.get(url="http://139.198.21.67:9080/test1",
        #                     headers={"Connection": "keep-alive",
        #                              "apikey": "test_api"})
        # print(resp.status_code, resp.json())
    print("all threads created successfully")
    t.close()
    print("closed")
    t.join()
    print("finished")
    print(50000000 / (time.time() - t0))


if __name__ == "__main__":
    main()
