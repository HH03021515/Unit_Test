# 在单机上利用多核处理器执行多个worker，
# 需要在设备管理器查看CPU有几个核心，worker的数量不能超过本机的处理器数，
# 建议不要全部占用，如8核CPU用6核:1主5从，留两核备用
# 主机：locust -f locustDemo.py --master
# 工作机：运行cmd命令打开多个新窗体进入路径运行命令locust -f locustDemo.py --worker
# 其他参数：-f后面跟路径+要执行的.py文件名，-c是设置并发用户数，-r是设置每秒进入用户数,-t设置运行时长
# Type：请求类型，即接口的请求方法； Name：请求路径；requests：当前已完成的请求数量；fails：当前失败的数量；
# Median：响应时间的中间值，即50%的响应时间在这个数值范围内，单位为毫秒；Average：平均响应时间，单位为毫秒；
# Min：最小响应时间，单位为毫秒；Max：最大响应时间，单位为毫秒；Content Size：所有请求的数据量，单位为字节；
# reqs/sec：每秒钟处理请求的数量，即QPS；

# 结果分析：每秒请求总数：如果上下波动较大，说明性能不稳定。
# 响应时间：黄色为最大时间，绿色为最小时间。一般3-5秒为最佳，超过10秒为较差，最大值如果持续高位就需要进行性能优化。

# 为何出现拐点，在某段时间tps直线下降，然后又迅速增大，再隔一段时间又重复这一现象？
# 分析：1、可能是python的垃圾回收机制占用了资源
# 2、压力测试时间久了，TPS就会抖动，而且越往后越厉害，说明资源释放有点问题，需要时间释放，然后才能回收，TPS才能提升
# 3、设置了最大的等待处理数, 超过负载了服务就自动丢弃了，出现这种情况就得扩容了

import sys
import time
from locust import task, events, User, HttpUser, TaskSet
# 使用FastHttpUser替代requests,提升5-6倍的并发量
from locust.contrib.fasthttp import FastHttpUser

class UserBehavior(TaskSet):
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
        self.client.get("/", name="打开百度首页")

    @task(1)
    def test_post(self):
        """由于没有免费的post接口，暂时用百度搜索"""
        self.client.post("/s?wd=etcp", name="使用百度搜索关键字etcp")


class WebUser(FastHttpUser):
    # class WebUser(HttpUser):   # 用requsts方法 rps可以很高，但失败事务也很高，用FastHttpUser失败事务很低但rps没有超过30，头疼
    """性能测试配置，换算配置"""
    # task_set = UserBehavior  # Testcase类,1.0的旧语法，已经废弃
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 3000
    host = "https://baidu.com"

