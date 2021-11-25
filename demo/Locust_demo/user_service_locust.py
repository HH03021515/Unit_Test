# 用户服务的查询及修改信息接口压测脚本

import sys
import time

from locust import task, events, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class User_Service(TaskSet):

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

    @task(7)
    def user_service(self):
        '''用户信息查询接口'''
        header = {
            "tenantId": 2021110300001,
        }
        res = self.client.get(
            'user/v1/query?userId=19146961&phoneNumber=13718415257', headers=header, name='用户信息查询接口（有数据）')
        if res.status_code != 200:
            print('Response error message is: ', res.text)
        else:
            pass

    @task(1)
    def user_service_nodata(self):
        '''用户信息查询接口'''
        header = {
            "tenantId": 2021110300001,
        }
        res = self.client.get(
            'user/v1/query?userId=0&phoneNumber=0', headers=header, name='用户信息查询接口（无数据）')
        if res.status_code != 200:
            print('Response error message is: ', res.text)
        else:
            pass

    @task(1)
    def userInfo_edit(self):
        '''用户信息修改接口'''
        header = {
            "tenantId": 2021110300001,
        }
        payload = {
            "phoneNumber": "13718415257",
            "sex": "MALE",
            "userId": 19146961
        }
        res = self.client.post(
            'user/v1/infoChange', headers=header, json=payload, name='用户信息修改接口（有数据）')
        if res.status_code != 200:
            print('Response error message is: ', res.text)
        else:
            pass

    @task(1)
    def userInfo_edit_nodata(self):
        '''用户信息修改接口'''
        header = {
            "tenantId": 2021110300001,
        }
        payload = {
            "phoneNumber": "13718415257",
        }
        res = self.client.post(
            'user/v1/infoChange', headers=header, json=payload, name='用户信息修改接口（无数据）')
        if res.status_code != 200:
            print('Response error message is: ', res.text)
        else:
            pass


class Web_User_Service(FastHttpUser):
    tasks = [User_Service]
    min_wait = 1000
    max_wait = 3000
    host = "http://user.intra.sit.etcp.net:80/"
