# author:ToddCombs
# 基准测试 ： 模拟单个用户访问系统的场景，考察系统性能指标，关注系统功能是否正常，为其他压测提供基准参考。
# 负载测试： 模拟系统在正常压力下(预期压力或者系统达到临界)的负载能力，判断是否满足业务需求。
# 压力测试 : 不断提升系统负载知道达到性能拐点，寻找系统最大负载能力，性能瓶颈等。
# 稳定性测试：在一定压力下持续运行，关注系统长期一定负载下是否能稳定服务。
#
# 作者：orientlu
# 链接：https://www.jianshu.com/p/a97c3aec1551
# 来源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#  服务器性能主要看：协议，并发，以及模拟真实业务场景
# locust对于loadrunner,jmeter的优势： 开源，python，协程，高并发，性能自动化测试平台
# 对于操作系统来说，线程是最小的执行单元，进程是最小的资源管理单元。
# 协程，英文Coroutines，是一种比线程更轻量级的存在，正如一个进程可以拥有多个线程一样，一个线程也可以拥有多个协程。
# 协程支持的语言：Lua5.0开始使用协程，通过扩展库coroutine来实现。
# Python可以通过yield/send方式实现协程，在Python3.5以后，async/await成为了更好的替代方案
# Go语言对协程的实现非常强大而简洁，可以轻松创建成百上千个协程并发执行。


# 本份文件主要优化了locust测试报告的文件内容。


from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    """继承自HttpUser类"""
    host = "http://test.valval.cool"  # 测试页
    wait_time = between(0, 0)  # 每个模拟用户等待1到2.5秒

    # 被task装饰的才会并发执行
    @task
    def api_one(self):
        """client属性是HttpSession实例，用来发送HTTP请求"""
        self.client.get("/api1")


    # 每个类只会有一个task被选中执行
    # 3代表weight权重
    # 权重越大越容易被选中执行
    # view_item比hello_world多3倍概率被选中执行
    @task
    def api_two(self):
        self.client.post("/api2", data={'key': 'value'})

        # name参数作用是把统计结果按照同一名称进行分组
        # 这里防止URL参数不同会产生10个不同记录不便于观察
        # 把10个汇总成1个"/item"记录
        #     self.client.get(f"/item?id={item_id}", name="/item")
        #     time.sleep(1)

    # 每个模拟用户开始运行时都会执行，固定搭配
    # def on_start(self):
    #     self.client.post("/login", json={"username": "18800000000", "password": "asd123456"})
