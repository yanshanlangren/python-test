# -*- coding: UTF-8 -*-
from flask import (
    Flask,
    jsonify,
    request,
)
from apscheduler.schedulers.background import BackgroundScheduler
from scrapy.stock_scrapy import (
    scrapy_daily_stock_info,
    get_data_from_csv
)

# import logging
# from logging.handlers import TimedRotatingFileHandler

app = Flask(__name__)


@app.route('/api/data', method=['GET'])
def get_data():
    # get stock data
    df = get_data_from_csv()

    # get request para
    code = int(request.values.get('code', 0))

    res = {}
    row_set = df[u'\u80A1\u7968\u4EE3\u7801']
    row = None
    for k, v in row_set.items():
        if v == code:
            row = k
            break

    for k, v in df.items():
        res[k] = v.get(row, "")
    response = {'success': 'true', 'message': res}
    return jsonify(response), 200


@app.route('/api/trigger', method=['GET'])
def get_data():
    trigger_daily_fetch_job()
    print("fetch job triggered")
    response = {'success': 'true', 'message': "OK"}
    return jsonify(response), 200


def trigger_daily_fetch_job():
    scrapy_daily_stock_info(1, 232)
    print("daily fetch job triggered")


# def initlogger():
#     formatter = logging.Formatter('%(name)-12s %(asctime)s level-%(levelname)-8s thread-%(thread)-8d %(message)s')  # 每行日志的前缀设置
#     log = logging.getLogger('api')
#     fileTimeHandler = TimedRotatingFileHandler(cf.LOG_API_PATH + 'api_', "S", 1, 10)
#     fileTimeHandler.suffix = "%Y%m%d.log"  # 设置 切分后日志文件名的时间格式 默认 filename+"." + suffix 如果需要更改需要改logging 源码
#     fileTimeHandler.setFormatter(formatter)
#     logging.basicConfig(level=logging.INFO)
#     fileTimeHandler.setFormatter(formatter)
#     log.addHandler(fileTimeHandler)


if __name__ == '_main__':
    # run flask app
    app.run(debug=True)

    # start daily task
    scheduler = BackgroundScheduler()
    scheduler.add_job(trigger_daily_fetch_job, 'cron', day_of_week='1,2,3,4,5', hour='15', minute='00', second='00')
    scheduler.start()
    print("daily fetch job created.")
