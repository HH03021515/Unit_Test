# 大鹏教育login页面登录性能测试
import base64
from locust import HttpUser, TaskSet, task
from random import choice

class Discuz_Login(TaskSet):

    @task(1)
    def index(self):
        url = "/login"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        self.client.get(url=url, headers=headers, name="登录首页")

    @task(1)
    def login(self):
        # userinfo = choice(self.locust.userdata)
        # userinfo = userinfo.split(",")
        # print(userinfo)
        url = "oauth/token"
        username = 'dapengbeijingservic'
        password = 'secretservice'
        token_string = base64.b64decode(username + ":" + password)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic {}".format(token_string).encode()
        }
        data = {"grant_type": "password", "username": 18800000000, "password": "asd123456", "code": ""}
        with self.client.post(url, headers=headers,  data=data, name="登录") as response:
            print(response.text)
            return response

class Discuz_User(HttpUser):
    tasks = [Discuz_Login]
    # 等待时间
    min_wait = 1000
    max_wait = 3000
    host = "https://test-zc.dapengjiaoyu.cn/"
    formdata = "grant_type=password&username=18800000000&password=asd123456&code="
    #
    # userdata = []
    # with open("data/userdata.csv", "r") as file:
    #     for line in file.readlines():
    #         userdata.append(line.strip())