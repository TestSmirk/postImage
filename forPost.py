import threading #线程.
from concurrent.futures import thread
import random

import requests#网络请求 requests.request
import time


def posts():
    url = "http://l:8002/c/add_static_label"

    import random
    querystring = {"category_name": random.randint(0, 5), "album_name": "this is label" + str(random.randint(0, 222))}
    print(querystring)
    headers = {
        'cache-control': "no-cache",
        'postman-token': "7484fe1f-3895-5255-0045-4e7e254f0146"
    }

    response = requests.request("POST", url, headers=headers, params=querystring)

    return response


# for i in range(0, 1000000):
#     print(posts().text)
exitFlag = 0


def testGet():
    url = "http://192.168.101.111:8001/a/new_home?category_name=1&user_id=5823d1954406b7368e2dd76c&limit=20&skip=0"

    print(requests.get(url).text)
    return requests.get(url).text


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        for i in range(0, 10000):
            print(testGet().text)


def posts():
    url = "http://l:8002/a/add_play_count"

    querystring = {"category_name": "1", "id": "589d33f44406b75c493d1a36"}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "aa40fa2f-74cd-c0e9-13b0-e303de3927c9"
    }

    response = requests.request("POST", url, headers=headers, params=querystring)
    return response


# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             thread.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1

# 创建新线程
# for x in range(0, 1000):
#     thread1 = myThread(x, "Thread-" + str(x), x)
#     thread1.start()

# print("Exiting Main Thread")
# testGet()
for i in range(0, 2000):
    print(posts().text)
