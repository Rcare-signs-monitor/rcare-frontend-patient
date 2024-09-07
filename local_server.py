from flask import Flask
from flask_cors import CORS
from threading import Thread
import requests
import json

task_num = 0

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():
    global task_num
    while True:
        if task_num == 1:
            res = requests.get("https://lot2024.site:442/signs/3?num=1&table=true") # 发送体征查询
            task_num = 0
            return {
                "type": 0,
                "data": json.loads(res.text)['data']
            }
        elif task_num == 2:
            res = requests.post("https://lot2024.site:442/calling", json={"id":3, "data":1}) # 发送呼叫
            task_num = 0
            return {
                "type": 1,
                "data": "sucess"
            }

# 点击用
@app.route('/api/sign')
def click1():
    res = requests.get("https://lot2024.site:442/signs/3?num=1&table=true") # 发送体征查询
    return json.loads(res.text)['data']
@app.route('/api/help')
def click2():
    res = requests.post("https://lot2024.site:442/calling", json={"id":3, "data":1}) # 发送呼叫
    return "sucess"

def test_set_flag(sec):
    global task_num
    import time
    import random
    while True: 
        time.sleep(random.randint(5, sec))
        task_num = 2

if __name__ == '__main__':
    # t1 = Thread(target=test_set_flag, args=(10, ))
    # t1.start()
    app.run(port=5111, debug=True)