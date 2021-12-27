# 停车记录重构接口压测脚本
import random

import numpy as np
import pandas as pd
from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class Parking_Record(TaskSet):
    # 获取csv文件里的所有列,存储到一个数组中
    data = np.array(pd.read_csv("demo/Locust_demo/10000_utf8.csv"))

    def on_start(self):
        '''测试套件开始时执行'''
        print("开始停车记录重构接口压测")

    @task(7)
    def search_carin(self):
        '''查询在场车停车记录-在场'''
        res = self.client.get(
            "carin/searchCarin?color=&plateNumber=" + str(random.choice(Parking_Record.data)[0]), name='查询在场车停车记录')
        if res.status_code != 200:
            print("请求报错了啊，错误信息：", res.text)
        else:
            pass


class Parking_Record_Test(FastHttpUser):
    tasks = [Parking_Record]
    min_wait = 1000
    max_wait = 3000
    host = "http://parking-record-webc.b.sit.etcp.net/"
