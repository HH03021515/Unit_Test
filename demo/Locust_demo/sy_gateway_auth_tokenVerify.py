# sy网关鉴权接口压测

import sys
import time

from locust import task, events, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class auth_tokenVerify(TaskSet):

    def on_start(self):
        print('开始压测p平台网关。。。')

    # def on_stop(self):
    #     print('运行时间：', time.strftime("%Y-%m-%d %H:%M:%S"))

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
    def test_auth_tokenVerify(self):
        '''鉴权接口'''
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'Host': 'authority.intra.sit.etcp.net',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language:': 'zh-CN,zh;q=0.9',
            'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6InAwMDIiLCJmdWxsTmFtZSI6IuadjuaXrSIsImV4cCI6MTYzNzEzNDU4MSwidXVpZCI6ImUzYzk0ZTBjLTVlYWUtNDZkNS05YTc4LThiMmE0MTQzNGE4OCIsInVzZXJJZCI6IjQyMjUiLCJpYXQiOjE2MzcxMzA5ODF9.gRSXs6-ThH7eG1pyGKNdMYzg195UG8dIxpZr4TMg8eA'
        }
        # response = self.client.post(
        #     "auth/auth/1/tokenVerify", header=header, name='网关鉴权tokenVerify接口')
        response = self.client.post("authority/auth/1/tokenVerify", headers=header, name='网关鉴权tokenVerify接口1')
        print("Response status code: ", response.status_code)
        print("Response content: ", response.text)

    # @task(1)
    # def test_auth_tokenVerify_error(self):
    #     '''鉴权接口传无效token'''
    #     header = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'token': '111111'
    #     }
    #     self.client.post(
    #         "/authority/auth/1/tokenVerify", header=header, name='网关鉴权tokenVerify接口（无效token）').text


class Web_gwp_tokenVerify(FastHttpUser):
    tasks = [auth_tokenVerify]
    min_wait = 1000
    max_wait = 3000
    # host = "http://gw-p.intra.sit.etcp.net/"  # 网关host
    host = "http://authority.intra.sit.etcp.net/"
