# mianshiya网站登录接口性能测试
from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class Mianshiya_Locust(TaskSet):

    def on_start(self):
        '''测试套件开始时执行'''
        print("对mianshiya网站登录接口压测")

    @task(1)
    def login_mianshiya(self):
        '''mianshiya登录接口'''
        res = self.client.get(
            "/login?captcha=111111", name='login接口')
        if res.status_code != 200:
            print("请求报错了啊，错误信息：", res.text)
        else:
            pass

class Mianshiya_Test(FastHttpUser):
    tasks = [Mianshiya_Locust]
    min_wait = 1000
    max_wait = 3000
    host = "https://mianshiya-2g3ifawi5a19f176-1256524210.ap-shanghai.app.tcloudbase.com"