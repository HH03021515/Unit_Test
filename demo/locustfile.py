# author:ToddCombs
import time

from locust import HttpUser, task, between

class QuickstarUser(HttpUser):
    """继承自HttpUser类"""

    wait_time = between(1, 2.5)  # 每个模拟用户等待1到2.5秒


    # 被task装饰的才会并发执行
    @task
    def hello_world(self):
        """client属性是HttpSession实例，用来发送HTTP请求"""
        self.client.get("/Hello")
        self.client.get("/World")

    # 每个类只会有一个task被选中执行
    # 3代表weight权重
    # 权重越大越容易被选中执行
    # view_item比hello_world多3倍概率被选中执行
    @task(3)
    def view_items(self):
        for item_id in range(10):
            # name参数作用是把统计结果按照同一名称进行分组
            # 这里防止URL参数不同会产生10个不同记录不便于观察
            # 把10个汇总成1个"/item"记录
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)

    # 每个模拟用户开始运行时都会执行，固定搭配
    def on_start(self):
        self.client.post("/login", json={"username": "foo", "password": "bar"})
