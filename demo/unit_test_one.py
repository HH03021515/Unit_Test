# author:ToddCombs
import unittest

# 继承测试用例
class forTest(unittest.TestCase):
    # 类的初始化，需要@classmethod装饰器
    @classmethod
    def setUpClass(cls) -> None:
        print('class')
    # 类的释放
    @classmethod
    def tearDownClass(cls) -> None:
        print('tclass')



    # 函数名必须以test开头，否则无法识别为一条测试用例
    def plus(self,a,b):
        c = a + b
        print(c)
        return c

    def test_c(self,):
        self.plus(1,2)
        print('c')



    # 初始化，用例执行之前执行
    def setUp(self) -> None:
        print('setUp')
    # 释放，用例执行之后执行
    def tearDown(self) -> None:
        print('tearDown')

    # 测试用例
    def test_a(self):
        print('a')

    def test_b(self):
        print('b')

if __name__ == '__main__':
    unittest.main()