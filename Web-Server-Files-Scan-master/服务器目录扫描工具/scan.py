import requests
import argparse
from multiprocessing import Pool
from datetime import datetime

value_list = []


# 读取字典值，将值保存在列表中
def get_dict(urls):
    if urls.endswith('/'):
        urls = urls.replace('/', '')
    with open('dict.txt', 'r') as f:
        for content in f.readlines():
            content = content.replace('\n', '')
            value_list.append(urls+content)


# 开始请求
def start_request(value):

    try:
        res = requests.get(value, timeout=2)
        if res.status_code == 200:
            print('[%s]  [%d]   %s' % (datetime.now().strftime('%H:%M:%S'), res.status_code, value))
    except Exception as e:
        print('Request Error')


# 使用命令行，获得网址
def order():
    global threading_number
    parse = argparse.ArgumentParser(description='Scanning The Server Files')
    parse.add_argument('-u', '-url', help='Input The Url Then Start To Scan')
    parse.add_argument('-n', '-number', default=5, type=int, help='Set The Number Of Threading(Default is 5)')
    args = parse.parse_args()
    url = args.u
    threading_number = args.n
    print('[%s]  [INFO]  Start To Scanning......\n' % (datetime.now().strftime('%H:%M:%S')))

    return url


def threads(number):
    pool = Pool(number)
    pool.map(start_request, value_list)
    pool.close()
    pool.join()


if __name__ == '__main__':
    threading_number = 0
    u = order()  # 获得网址
    get_dict(u)  # 将网址加入字典
    threads(threading_number)
    print('\n[End]')
