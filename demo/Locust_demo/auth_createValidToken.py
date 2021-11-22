# 生成有效token，测试接口

import sys
import time

from locust import task, events, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class auth_tokenVerify(TaskSet):

    def on_start(self):
        print('开始压测p平台网关。。。')

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
    def test_auth_tokenVerify_params(self):
        '''生成有效token接口'''
        payload = {"appid": "p001", "userId": 4251}
        response = self.client.post(
            "authority/auth/1/createValidToken", content_type="application/x-www-form-urlencoded", data=payload,
            name="获取token")
        print("Response content: ", response.text)


class Web_gwp_tokenVerify(FastHttpUser):
    tasks = [auth_tokenVerify]
    min_wait = 1000
    max_wait = 3000
    host = "http://authority.intra.sit.etcp.net/"
