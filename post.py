import requests

if __name__ == '__main__':
    while True:
        r = requests.post("https://sm.ms/api/upload", files={'smfile': open('pycharm.png', 'rb')},
                          data={"format": "xml"})
        print(r.text)

        # r = requests.post("http://192.168.1.217:8001/a/baseinfo",files={'head_image': open('pycharm.png','rb')},data={"_id":"5823d1954406b7368e2dd76c"})
        # print(r.text)
