import copy
import logging
import telnetlib
import time

from icecream import ic

from zbtest.utils.logs import file_logger

logger = logging.getLogger(__name__)


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
        file_logger.debug(f"调用命令是：{cmd}")
        resp0 = None
        try:
            if self.login_flag:
                resp0 = self.telnet_client.execute_some_command(cmd)
                ic(f"接口响应是,resp={resp0}")
                file_logger.debug(f"接口响应是,resp={resp0}")
                return resp0
            else:
                ic("登陆失败！")
                file_logger.debug("登陆失败！")
        except Exception as e:
            file_logger.error(f"调用接口异常, 接口响应是resp={resp0}, 异常信息为：{e}")
            raise Exception(f"调用接口异常, 接口响应是resp={resp0}, 异常信息为：{e}")
