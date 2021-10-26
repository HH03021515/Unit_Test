import sys
import time

from locust import HttpUser, TaskSet, task, events


class UserBehavior(HttpUser):
    """Locust任务集，定义每个locust行为"""

    def on_start(self):
        print("运行压测前置条件")

    def get_response(self, response):
        """
        获取返回
        :param response:请求返回对象
        :return:
        """
        start_time = int(time.time())
        if response.status_code == 200:
            events.request_success.fire(
                request_type="recv",
                name=sys._getframe().f_code.co_name,
                response_time=int(time.time() - start_time) * 1000,
                response_length=0
            )
        else:
            events.request_failure.fire(
                request_type="recv",
                name=sys._getframe().f_code.co_name,
                response_time=int(time.time() - start_time) * 1000,
                response_length=0,
                exception=f"Response Code Error! Code:{response.content}"
            )

    @task(1)
    def test_get(self):
        self.client.get("https://baidu.com", name="打开百度首页")

    @task(1)
    def test_post(self):
        """由于没有免费的post接口，暂时用百度搜索"""
        self.client.post("https://baidu.com/s?wd=etcp", name="使用百度搜索关键字etcp")


class WebUser(TaskSet):
    """性能测试配置，换算配置"""
    task_set = UserBehavior  # Testcase类
    host = "https://baidu.com"
    min_wait = 1000
    max_wait = 3000

#
# class TestLocust(HttpLocust):
#     """自定义locust类，可设置Locust的参数"""
#     tast_set = UserBeHavior
#     host = "https://www.baidu.com"  # 被测域名/服务器地址
#     min_wait = 5000
#     # 最小等待时间，至少等待多少秒后Locust选择执行一个任务。
#
#     max_wait = 9000
#     # 最大等待时间，最多等待多少秒后Locust选择执行一个任务。
