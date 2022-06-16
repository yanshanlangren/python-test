import requests
import time
import sys
import threading
from optparse import OptionParser

global_success = 0
global_time = 0
url = ""


def _get_opt_parser():
    parser = OptionParser('''%prog -p <port>''')
    parser.add_option("-p", "--port", action="store", type="int", dest="port", help='''port''', default=9080)
    parser.add_option("-n", "--count", action="store", type="int", dest="count", help='''count''', default=10000)
    parser.add_option("-t", "--thread", action="store", type="int", dest="thread", help='''thread''', default=100)
    return parser


def looper(count):
    global url
    total_count = int(count)
    total_time = 0.0
    success = 0
    for i in range(total_count):
        t = time.time()
        resp = requests.get(url=url)
        total_time += time.time() - t
        if resp.status_code == 200:
            success += 1
    global global_success
    global global_time
    global_success += success
    global_time += total_time


def main(args):
    options, _ = _get_opt_parser().parse_args(args)
    port = options.port
    total_count = options.count
    thread_count = options.thread

    global url
    url = "http://192.168.0.53:%d/test" % port
    print("url[%s], total_count[%s]" % (url, total_count))
    print("start testing...")
    threads = []
    for i in range(thread_count):
        t = threading.Thread(target=looper, args=(total_count,))
        threads.append(t)
    t0 = time.time()
    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()
    t = time.time() - t0
    global global_success
    global global_time
    print("test finished, total_count %d, average time %f ms, success rate %s, send rate %f." % (
        total_count * thread_count, global_time * 1000 / (total_count * thread_count),
        global_success * 1.0 / (total_count * thread_count), total_count * thread_count * 1.0 / t))


if __name__ == '__main__':
    main(sys.argv[1:])
