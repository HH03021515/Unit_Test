# 微信支付相关接口压测
import sys
import time

from locust import task, events, TaskSet
from locust.contrib.fasthttp import FastHttpUser

class UserBehavior(TaskSet):
    """Locust任务集，定义每个locust行为"""

    def on_start(self):
        print("微信接口压测准备。。。")

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
    def test_getqueryPayOrder(self):
        self.client.get("/orderquery/version/queryPayOrder?innerorderid=4A7ED092-E22C-4B2D-9B1A-E2B7290D40FA",
                        name='第三方订单查询接口（有结果）')

    @task(1)
    def test_getquertPayOrder_nodata(self):
        self.client.get("/orderquery/version/queryPayOrder?innerorderid=4A7ED092-E22C-4B2D-9B1A-E2B7290D1111",
                        name='第三方订单查询接口（无结果）')

    @task(1)
    def test_paymentRest(self):
        header = {
            "Content-Type": "application/json",
        }
        payload = {
        "appId": "wxcc603d9f0d54eaf0", "goodsTag": "", "innerOrderId": "C53129C6-634F-4F27-A0EA-2E9E60341CAF",
         "openId": "", "payAmount": "11.00", "payBusinessType": "PARKING_TEMP",
         "senceInfo": "{\"start_time\":\"2021-11-08T11:02:41+08:00\",\"plate_color\":\"BLUE\",\"device_id\":\"724\",\"end_time\":\"2021-11-08T14:05:53+08:00\",\"parking_id\":\"01000076482316363405638875052\",\"charging_duration\":10992,\"plate_number\":\"豫Q59M86\",\"parking_name\":\"李朗国际珠宝产业园\"}",
         "tradeBizInfo": {"parkingCmbClearing": False, "parkingDirectClearing": False, "parkingId": 724,
                          "parkingIsWanDa": False}}
        self.client.post("/paymentRest/crePayOrd4WxWithHoldRecord", json=payload, header=header, name='微信支付分代扣接口')

class WebUser(FastHttpUser):
    """性能测试配置"""

    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 3000
    host = "http://newpay.qa.etcp.cn/service"
