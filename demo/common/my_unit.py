# 封装的unittest钩子函数公共类
import unittest

class MyUnit(unittest.TestCase):

    # 测试类之前的准备工作，需要装饰器classmethod，建议返回none
    @classmethod
    def setUpClass(cls) -> None:
        print("测试类之前的准备工作:连接数据库，创建日志对象。")

    # 测试类之后的扫尾工作，需要装饰器classmethod，建议返回none
    @classmethod
    def tearDownClass(cls) -> None:
        print("测试类之后的扫尾工作：销毁数据库连接，销毁日志对象。")

    # 测试开始前的准备工作，建议返回none
    def setUp(self) -> None:
        print("测试用例之前的准备工作：打开浏览器，加载网页")

    # 测试结束后的准备工作，建议返回none
    def tearDown(self) -> None:
        print("测试用例之后的工作：关闭浏览器")