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
# 小提示：
# 在压测时，尽量将搭建被测服务的机器与生产环境的机器设备保持一致，运行脚本的机器尽量选择好一点的，网络不要选择公司内部网络
# 在虚拟用户选择时，先从低到高选择，比如先50，100，200类似这样选择，递推虚拟用户数后，注意观察TPS有没有明显的增加或下降，
# 查看被测服务机器的CPU,内存等信息，注意看有没有GC问题
# 在性能测试时，内存泄漏问题，在程序运行的一段时间，虚拟用户数达到了预设值，内存会先升高后，持续一段时间的稳定，
# 没有明显的增加或减少，如果当虚拟用户数达到了预设值，内存还继续上升的话，可能会有GC问题。

# 1.如果在Linux服务器运行locust，尴尬的是没有图形界面操作web。
# 解决措施：一般连接服务器都是通过xshell来连接，我们可以通过xshell自带隧道功能建立一条隧道，将服务器8089端口的信息传输到本地计算机，
# 这样直接在本地计算的浏览器就能对服务器进行控制。
# xshell >隧道窗格>转移规则>右键添加
# 2.后台运行命令，防止命令中断
# 通过xshell访问到服务器后，如果运行locust -f locu.py --master ，一旦xshell退出，命令也会自动中断。
# 因为通过xshell登录所运行命令都属于登录用户进程的子进程，一旦断开连接主进程会自动关闭，该进程下所有命令都会自动关闭。所以如果是长时间运行的话最好把命令放在后台运行。
# (locust -f load.py --master &)   该命令表示把该进程放置到后台运行，就算用户断开连接也会一直运行。
# 放置到后台后果想要关闭命令就先使用ps -ef|grep locust 查看进程号，再用kill pid 来杀掉进程。
# 3.用户数量的详细解释web界面的user 数量表示并发数，也就是每次访问的并发连接数。实践的时候用户数量是300，表示每次访问有300个用户同时访问，
# 吞吐量能达到2000/s，说明在一秒的时间内服务器响应了大约7次，那么300的用户耗费的时间就是140ms左右。
# 4.用户数量与slvae关系用户数量是300，slave为3，那么每个slave会平均分配发送的用户量100，与jmerter分布式不一样。
# 五、最终测试结果 服务器配置：CPU 8核 内存16G  承受最大业务量900万次请求数，占用内存12G，占用磁盘空间23G。redis与业务量关系 80万请求数占用1G redis内存
# 磁盘与业务量关系  80万请求数占用2G 磁盘空间

# 由于IO操作非常耗时，程序经常会处于等待状态,比如请求多个网页有时候需要等待，gevent可以自动切换协程
# 遇到阻塞自动切换协程，程序启动时执行monkey.patch_all()解决
# from gevent import monkey
# monkey.patch_all()

import sys
import time
from locust import task, events, TaskSet
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
    # task_set = UserBehavior # Testcase类,1.0的旧语法，已经废弃
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 3000
    host = "https://baidu.com"
