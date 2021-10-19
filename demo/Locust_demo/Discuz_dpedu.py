# 大鹏教育login页面登录性能测试

from locust import HttpUser, TaskSet, task


class Discuz_Login(TaskSet):

    @task(2)
    def index(self):
        url = "/login"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        self.client.get(url=url, headers=headers, name="登录首页")

    @task(1)
    def login(self):
        # userinfo = choice(self.locust.userdata)
        # userinfo = userinfo.split(",")。0
        # print(userinfo)

        url = "basicdata/system/dict/find_by_type"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "Content-Type": "application/json",
        }
        # headers["Authorization"] = "Bearer " + getattr(Discuz_Login, 'login')
        data = {
            "grant_type": "password",
            "username": 18800000000,
            "password": "asd123456",
            "scope": "serviceclient"
        }

        with self.client.post(url, headers=headers, data=data, name="登录") as response:
            print(response.text)
            return response


class Discuz_User(HttpUser):
    tasks = [Discuz_Login]
    # 等待时间
    min_wait = 1000
    max_wait = 3000
    host = "https://test-zc.dapengjiaoyu.cn/"
    #
    # userdata = []
    # with open("data/userdata.csv", "r") as file:
    #     for line in file.readlines():
    #         userdata.append(line.strip())


if __name__ == '__main__':
    pass
