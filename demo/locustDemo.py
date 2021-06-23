from locust import HttpLocust, TaskSet, task

class UserBeHavior(TaskSet):
    """Locust任务集，定义每个locust行为"""
    @task(1)    # 任务权重值，多任务可定义不同权重值
    def get_root(self):
        """模拟发送数据"""
        response = self.client.get('/Hellooooo!', name='get_root')
        if not response.ok:
            print(response.text)
            response.failure('Got wrong response')

    @task(1)
    def index1(self):
        r = self.client.get('/test/index.html')
        print(r.text)

    @task(2)
    def search1(self):
        r = self.client.get('/test/search.html')
        print(r.text)





class TestLocust(HttpLocust):
    """自定义locust类，可设置Locust的参数"""
    tast_set = UserBeHavior
    host = "https://www.baidu.com"  # 被测域名/服务器地址
    min_wait = 5000
    # 最小等待时间，至少等待多少秒后Locust选择执行一个任务。

    max_wait = 9000
    # 最大等待时间，最多等待多少秒后Locust选择执行一个任务。



