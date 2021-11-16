# shenyu_gateway_locust 新网关鉴权接口压力测试
import sys
import time

# from gevent import monkey
# monkey.patch_all()
from locust import task, events, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class NoobGateway(TaskSet):

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

    # @task(1)
    # def test_gateway_debug(self):
    #     self.client.get(
    #         "/opendata/mrg/debug", name='debug接口压测')

    # @task(1)
    # def test_gateway_ok(self):
    #     self.client.get(
    #         "/bsapi2/ok.html", name='ok接口压测')

    @task(1)
    def test_getSwitch(self):
        '''对外网关接口'''
        header = {
            # 'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        self.client.get(
            "/rest/payment/switch/getSwitch", name='网关getSwitch接口压测')



class Web_gwp(FastHttpUser):
    tasks = [NoobGateway]
    min_wait = 1000
    max_wait = 3000
    host = "http://gw-p.intra.sit.etcp.net"  # 网关host
    # host = "http://paymentswitch.intra.uat.etcp.net"  # 内部host
