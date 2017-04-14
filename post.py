import os
import re
import threading

import requests

import json

import queue


def upload_file(file):
    file = str(file)
    r = requests.post("https://sm.ms/api/upload", files={'smfile': open(file, 'rb')},
                      data={"format": "json"})
    dict = json.loads(r.text)
    if str(dict['code']) == "success":
        print(dict['data']["url"])
    else:
        print("false")

threads = []
t1 = threading.Thread(target=upload_file,args="")
def getFiles(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            if re.match('jpg|.png', name[-4:]):
                print(root)

                q = queue.Queue()
                q.put(root + "/" + name)
                upload_file(root + "/" + name)
                #     print(os.path.join(root, name))

def test():
    print("test")

getFiles("/home/testsmirk/Pictures/")


def postChat(str):
    r = requests.get("http://op.juhe.cn/robot/index",{
        #这个key要自己申请/
        "key": "",  # 您申请到的本接口专用的APPKEY
        "info":str ,  # 要发送给机器人的内容，不要超过30个字符

    })
    print(r.json().get("reason"))

postChat("天气")
# r = requests.post("http://192.168.1.217:8001/a/baseinfo",files={'head_image': open('pycharm.png','rb')},data={"_id":"5823d1954406b7368e2dd76c"})
# print(r.text)

