# 配合会员重构接口压测
from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class TestUser_Annotation(TaskSet):

    def on_start(self):
        print('开始压测p平台用户服务。。。')

    @task(1)
    def test_annotation(self):
        '''annotation接口'''
        res = self.client.get('/annotation', name='annotation接口')
        if res.status_code != 200:
            print('Response error message is: ', res.text)
        else:
            pass


class Web_Test_Annotation(FastHttpUser):
    tasks = [TestUser_Annotation]
    min_wait = 1000
    max_wait = 3000
    host = "http://user.intra.sit.etcp.net"
