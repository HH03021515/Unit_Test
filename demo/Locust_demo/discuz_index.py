# 更新版本locust已经不用HttpLocust，而使用HttpUser了
# 简单写了个压https://baidu.com/more的
from locust import HttpUser, TaskSet, task


class Discuz_Task(TaskSet):

    @task(1)
    def index(self):
        self.client.get("/more")


class Discuz_Locust(HttpUser):
    tasks = [Discuz_Task]
    host = "https://baidu.com"
    min_wait = 1000
    max_wait = 2000
