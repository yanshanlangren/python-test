# -*- coding: UTF-8 -*-
import re
import time
# import pymongo
import requests
import pandas as pd
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
}

data_dir = 'C:\\Users\\Elvis\\Desktop\\data\\'


def get_page(url):
    """获取网页源码"""
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.ConnectionError as e:
        print('Error', e.args)


def get_stock_data(text):
    """获取股票代码、名称、PE"""
    com = re.compile('"f2":(?P<end>.+?),'  # 最新价
                     '.*?"f3":(?P<fluctuation>.+?),'  # 涨跌幅
                     '.*?"f4":(?P<change_amount>.+?),'  # 涨跌额
                     '.*?"f5":(?P<trading_amount>.+?),'  # 成交量(手)
                     '.*?"f6":(?P<trading_volume>.+?),'  # 成交额
                     '.*?"f7":(?P<zhenfu>.+?),'  # 振幅
                     '.*?"f8":(?P<huanshoulv>.+?),'  # 换手率
                     '.*?"f9":(?P<shiyinglv_dongtai>.+?),'  # 市盈率(动态)
                     '.*?"f10":(?P<liangbi>.+?),'  # 量比

                     # '.*?"f11":(?P<liangbi>.+?),'  # 量比

                     '.*?"f12":"(?P<number>.+?)",'  # 股票代码
                     '.*?"f13":(?P<gupiaoleixing>.+?),'  # 股票类型
                     '.*?"f14":"(?P<name>.+?)",'  # 股票名称
                     '.*?"f15":(?P<max>.+?),'  # 最高
                     '.*?"f16":(?P<min>.+?),'  # 最低
                     '.*?"f17":(?P<start>.+?),'  # 今开
                     '.*?"f18":(?P<zuoshou>.+?),'  # 昨收

                     # '.*?"f20":(?P<?>.+?),'  # 今开
                     # '.*?"f21":(?P<start>.+?),'  # 今开
                     # '.*?"f22":(?P<start>.+?),'  # 今开

                     '.*?"f23":(?P<shijinglv>.+?),',  # 市净率

                     # '.*?"f24":(?P<shijinglv>.+?),'  # 市净率
                     # '.*?"f25":(?P<shijinglv>.+?),'  # 市净率
                     # '.*?"f62":(?P<shijinglv>.+?),'  # 市净率
                     # '.*?"f115":(?P<shijinglv>.+?),'  # 市净率
                     # '.*?"f128":(?P<shijinglv>.+?),'  # 市净率
                     # '.*?"f140":(?P<shijinglv>.+?),'  # 市净率
                     # '.*?"f141":(?P<start>.+?),'  # 今开
                     # '.*?"f136":(?P<start>.+?),'  # 今开
                     # '.*?"152":(?P<start>.+?),'  # 今开
                     re.S)
    # com = re.compile('"f2":(?P<end>.+?),.*?"f6":(?P<volume>.+?),.*?"f12":"(?P<number>.+?)",.*?"f14":"(?P<name>.+?)"'
    #                  ',.*?"f15":(?P<max>.+?),.*?"f16":(?P<min>.+?),.*?"f17":(?P<start>.+?),', re.S)
    ret = com.finditer(text)
    for i in ret:
        yield {
            'number': i.group('number'),
            'fluctuation': i.group('fluctuation'),
            'change_amount': i.group('change_amount'),
            'trading_amount': i.group('trading_amount'),
            'trading_volume': i.group('trading_volume'),
            'zhenfu': i.group('zhenfu'),
            'huanshoulv': i.group('huanshoulv'),
            'shiyinglv_dongtai': i.group('shiyinglv_dongtai'),
            'liangbi': i.group('liangbi'),
            'gupiaoleixing': i.group('gupiaoleixing'),
            'name': i.group('name'),
            'start': i.group('start'),
            'max': i.group('max'),
            'min': i.group('min'),
            'zuoshou': i.group('zuoshou'),
            'shijinglv': i.group('shijinglv'),
            'end': i.group('end')
        }


def format_data(number=None, name=None, start_price=None, max_price=None, min_price=None, end_price=None, volume=None,
                fluctuation=None, change_amount=None, trading_amount=None, zhenfu=None, huanshoulv=None, shiyinglv_dongtai=None,
                liangbi=None, gupiaoleixing=None, zuoshou=None, shijinglv=None):
    """存进MongoDB"""
    # client = pymongo.MongoClient("localhost", 27017)
    # db = client.stock
    # collection = db.stock_data7
    shijian = time.strftime('%Y-%m-%d', time.localtime())  # '2020-05-25'
    data = {
        "日期": shijian,
        "股票代码": number,
        "股票名称": name,
        "今开": start_price,
        "最高": max_price,
        "最低": min_price,
        "最新价": end_price,
        "成交额": volume,

        "涨跌幅": fluctuation,
        "涨跌额": change_amount,
        "成交量(手)": trading_amount,
        "振幅": zhenfu,
        "换手率": huanshoulv,
        "市盈率(动态)": shiyinglv_dongtai,
        "量比": liangbi,
        "股票类型": gupiaoleixing,
        "昨收": zuoshou,
        "市净率": shijinglv,
    }
    # print(name)
    return data
    # collection.insert_one(data)


# def save_csv():
#     for code in CodeList:
#         print('正在获取股票%s数据' % code)
#         url = 'http://quotes.money.163.com/service/chddata.html?code=0' + code + \
#               '&end=20161231&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
#         urllib.request.urlretrieve(url, filepath + code + '.csv')


def scrapy_daily_stock_info(start=1, end=1):
    total = []
    for i in range(start, end + 1):
        url = 'http://60.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112408744624686429123_1578798932591&pn=' \
              '%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:' \
              '0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,' \
              'f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1586266306109' % i
        content = get_page(url=url)
        data = get_stock_data(text=content)
        for j in data:
            number = j.get('number')
            name = j.get('name')
            start = j.get('start')
            max_price = j.get('max')
            min_price = j.get('min')
            end = j.get('end')
            volume = j.get('trading_volume')
            # new para
            fluctuation = j.get("fluctuation")
            change_amount = j.get("change_amount")
            trading_amount = j.get("trading_amount")
            zhenfu = j.get("zhenfu")
            huanshoulv = j.get("huanshoulv")
            shiyinglv_dongtai = j.get("shiyinglv_dongtai")
            liangbi = j.get("liangbi")
            gupiaoleixing = j.get("gupiaoleixing")
            zuoshou = j.get("zuoshou")
            shijinglv = j.get("shijinglv")

            if start == '"-"':
                start, max_price, min_price, end, volume = '0', '0', '0', '0', '0'
            data_set = format_data(number=number, name=name, start_price=eval(start), max_price=eval(max_price),
                                   min_price=eval(min_price), end_price=eval(end), volume=round(eval(volume) / 10 ** 8, 2),
                                   fluctuation=fluctuation, change_amount=change_amount, trading_amount=trading_amount,
                                   zhenfu=zhenfu, huanshoulv=huanshoulv, shiyinglv_dongtai=shiyinglv_dongtai, liangbi=liangbi,
                                   gupiaoleixing=gupiaoleixing, zuoshou=zuoshou, shijinglv=shijinglv)
            total.append(data_set)
            # time.sleep(2)
    pd.DataFrame(total).to_csv('%s%s.csv' % (data_dir, time.strftime('%Y-%m-%d', time.localtime())),
                               encoding="utf-8-sig")
    return "OK"


def get_data_from_csv(date=time.strftime('%Y-%m-%d', time.localtime())):
    file_name = "%s%s.csv" % (data_dir, date)
    df = pd.read_csv(file_name)
    return json.loads(df.to_json())

print('a'
      'b')

scrapy_daily_stock_info(1, 232)
# df = get_data_from_csv()
# code = 600218
# res = {}
# row_set = df[u'\u80A1\u7968\u4EE3\u7801']
# row = None
# for k, v in row_set.items():
#     if v == code:
#         row = k
#         break
#
# for k, v in df.items():
#     res[k] = v.get(row, "")
# print(json.dumps(res).encode("utf-8"))
# code = "600218"
# print(int(code))
