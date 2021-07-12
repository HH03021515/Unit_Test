from locust import HttpLocust, TaskSet, task

class WebsiteTask(TaskSet):

    def on_start(self):
        self.client.post("/login",{
            "username": "test",
            "password": "123456"
        })


    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/about/")


class WebsiteUser(HttpLocust):

    task_set = WebsiteTask

    host = "http://debugtalk.com"
    min_wait = 1000
    max_wait = 5000
