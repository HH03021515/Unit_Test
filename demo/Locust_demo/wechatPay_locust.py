# 微信支付相关接口压测
import copy
import sys
import telnetlib
import time

from icecream import ic
from locust import task, events, TaskSet, User
from locust.contrib.fasthttp import FastHttpUser
from pyarrow import json


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
        self.client.get("http://newpay.qa.etcp.cn/service/orderquery/version/queryPayOrder?innerorderid=4A7ED092-E22C-4B2D-9B1A-E2B7290D40FA",
                        name='第三方订单查询接口（有结果）')

    @task(1)
    def test_getquertPayOrder_nodata(self):
        self.client.get("http://newpay.qa.etcp.cn/service/orderquery/version/queryPayOrder?innerorderid=4A7ED092-E22C-4B2D-9B1A-E2B7290D1111",
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
        self.client.post("http://newpay.qa.etcp.cn/service/paymentRest/crePayOrd4WxWithHoldRecord", json=payload, header=header, name='微信支付分代扣接口')


class DubboTask(TaskSet):
    def on_start(self):
        print("RPC接口压测准备。。。")

    @task(1)
    def test_dubbo_createPayOrder4WXPublicID(self):
        payload = {
            "appId": "wxcc603d9f0d54eaf0", "goodsTag": "", "innerOrderId": "C53129C6-634F-4F27-A0EA-2E9E60341CAF",
            "openId": "", "payAmount": "11.00", "payBusinessType": "PARKING_TEMP",
            "senceInfo": "{\"start_time\":\"2021-11-08T11:02:41+08:00\",\"plate_color\":\"BLUE\",\"device_id\":\"724\",\"end_time\":\"2021-11-08T14:05:53+08:00\",\"parking_id\":\"01000076482316363405638875052\",\"charging_duration\":10992,\"plate_number\":\"豫Q59M86\",\"parking_name\":\"李朗国际珠宝产业园\"}",
            "tradeBizInfo": {"parkingCmbClearing": False, "parkingDirectClearing": False, "parkingId": 724,
                             "parkingIsWanDa": False}}
        self.client.invoke_dubbo_api('createPayOrder4WXPublicID', 'payment', payload)


class GrpcUser(User):
    abstract = True

    stub_class = None

    def __init__(self, environment):
        super().__init__(environment)
        for attr_value, attr_name in ((self.host, "host"), (self.stub_class, "stub_class")):
            if attr_value is None:
                raise LocustError(f"You must specify the {attr_name}.")
        self._channel = grpc.insecure_channel(self.host)
        self._channel_closed = False
        stub = self.stub_class(self._channel)
        self.client = GrpcClient(stub)


class HelloGrpcUser(GrpcUser):
    host = "localhost:50051"
    stub_class = hello_pb2_grpc.HelloServiceStub

    @task
    def sayHello(self):
        if not self._channel_closed:
            self.client.SayHello(hello_pb2.HelloRequest(name="Test"))
        time.sleep(1)


class TelnetDubboClient:
    def __init__(self, host, port):
        self.handler = InvokeDubboApi(host, port)

    def __getattr__(self, name):
        func = getattr(self.handler, name)

        def wrapper(*args, **kwargs):
            request_meta = {
                "request_type": "telnet_dubbo",
                "name": name,
                "start_time": time.time(),
                "response_length": 0,
                "exception": None,
                "context": None,
                "response": None,
            }
            start_perf_counter = time.perf_counter()
            try:
                request_meta["response"] = func(*args, **kwargs)
            except Exception as e:
                request_meta["exception"] = e
            request_meta["response_time"] = (time.perf_counter() - start_perf_counter) * 1000
            events.request.fire(**request_meta)
            return request_meta["response"]

        return wrapper


class InvokeDubboApi(object):

    def __init__(self, server_host, server_post):
        try:
            self.telnet_client = TelnetClient(server_host, server_post)
            self.login_flag = self.telnet_client.connect_dubbo()
        except Exception as e:
            ic(f"invokedubboapi init error: {e}")

    def get_all_dubbo_apis(self):
        """ 获取指定服务的接口数量及接口明细
        """

        dubbo_apis = []

        try:
            if self.login_flag:
                services = self.telnet_client.execute_some_command("ls")
                ic(f"获取服务列表:{services}")
                services = services.split("\r\n")
                services.pop()

                for service in services:
                    resp = self.telnet_client.execute_some_command("ls {}".format(service))
                    resp = resp.split("\r\n")
                    resp.pop()
                    for j in range(len(resp)):
                        resp[j] = service + '.' + resp[j]
                        dubbo_apis.append(resp[j])
                new_dubbo_api_list = list(set(dubbo_apis))
                ic(f"rpc接口数量是: {len(new_dubbo_api_list)}")
                return new_dubbo_api_list
        except Exception as e:
            raise Exception(f"获取dubbo接口失败，原因是{e}")

    def invoke_dubbo_api(self, dubbo_service, dubbo_method, *obj):
        def clean(param):
            args = copy.deepcopy(param)
            if isinstance(args, dict):
                for k, v in args.items():
                    if isinstance(v, bool):
                        args[k] = str(v).lower()
                    elif isinstance(v, list):
                        args[k] = clean(v)
            elif isinstance(args, list):
                args = [clean(item) for item in param]

            return args

        cmd = f"invoke {dubbo_service}.{dubbo_method}{obj}"
        ic(f"调用命令是：{cmd}")
        resp0 = None
        try:
            if self.login_flag:
                resp0 = self.telnet_client.execute_some_command(cmd)
                ic(f"接口响应是,resp={resp0}")
                return resp0
            else:
                ic("登陆失败！")
        except Exception as e:
            raise Exception(f"调用接口异常, 接口响应是resp={resp0}, 异常信息为：{e}")


class TelnetClient(object):
    """通过telnet连接dubbo服务, 执行shell命令, 可用来调用dubbo接口
    """

    def __init__(self, server_host, server_post):
        self.tn = telnetlib.Telnet()
        self.server_host = server_host
        self.server_port = server_post

    # 此函数实现telnet登录主机
    def connect_dubbo(self):
        try:
            ic(f"telent连接dubbo服务端: telnet {self.server_host} {self.server_port}……")
            self.tn.open(self.server_host, port=self.server_port)
            return True
        except Exception as e:
            ic(f'连接失败, 原因是: {e}')
            return False

    # 此函数实现执行传过来的命令，并输出其执行结果
    def execute_some_command(self, command):
        # 执行命令
        cmd = (command + '\n').encode("gbk")
        self.tn.write(cmd)

        # 获取命令结果,字符串类型
        retry_count = 0
        # 如果响应未及时返回,则等待后重新读取，并记录重试次数
        result = self.tn.read_very_eager().decode(encoding='gbk')
        while result == '':
            time.sleep(1)
            result = self.tn.read_very_eager().decode(encoding='gbk')
            retry_count += 1
        return result


class WebUser(FastHttpUser):
    """性能测试配置"""

    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 3000
    # host = "http://newpay.qa.etcp.cn/service"

    # url = {"qa": ("10.103.22.92", 20992)}
