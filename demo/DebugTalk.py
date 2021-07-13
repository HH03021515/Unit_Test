from locust import HttpUser, TaskSet, task

class WebsiteTask(TaskSet):

    def on_start(self):
        self.client.post("/login", {
            "username": "test",
            "password": "123456"
        })

    # 请求两次/ 请求一次/about/
    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/about/")

    @task(1)
    def test_job1(self):
        self.client.get("/job1")

    @task(2)
    def test_job2(self):
        self.client.get("/job2")




class WebsiteUser(HttpUser):

    tasks = [WebsiteTask]

    host = "http://debugtalk.com"
    # 两次请求间隔1-5秒的随机值
    min_wait = 1000
    max_wait = 5000
