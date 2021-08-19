# **unittest与pytest的差异**

主流python自动化测试框架(占市场80%份额)：unittest,pytest
主流java自动化测试框架(占市场20%份额)：junit,testng

`unittest用例规则：`
1、测试文件必须导包，import unittest
2、测试类必须继承于unittest.TestCase
3、测试函数必须以test_为开头

`pytest用例规则：`
1、测试文件名必须以test_开头或_test结尾
2、测试类名必须以Test开头
3、测试函数必须以test_开头；
`注意：unittest必须继承于框架，而pytest不用继承于框架是单独独立的。`
unittest是耦合性的，pytest属于非耦合性的

`测试用例的夹具(前后置，钩子函数):`
unittest
setUp/tearDown    在测试用例之前和之后执行
setUpClass/tearDownClass  在测试类之前和之后执行
setUpModule/tearDownModule    在测试模块之前和之后执行
pytest
setup/teardown    在测试用例之前和之后执行
setup_class/teardown_class  在测试类之前和之后执行
setup_module/teardown_module    在测试模块之前和之后执行

`其他的夹具(前后置，钩子函数)：`
@pytest.fixtrue()

`断言：`
unittest:
self.assertEqual()
self.assertIn()
pytest:
python自带的aseet

`报告：`
unittest:
HTMLTestRunner.py
pytest:
pytest-html,allure插件

`失败重跑：`
unittest:
没有
pytest:
pytest-rerunfailures

`参数化：`
unittest:
ddt
pytest:
@pytest.mark.parametrize()

## 单元测试框架的作用
1、发现测试用例
2、执行测试用例
3、判断测试结果
4、生成测试报告

## unittest的重要组件
TestCase测试用例：最小业务逻辑单元
TestSuite测试套件：一组测试用例或测试套件的集合
TestFixtrue测试夹具：执行测试用例之前和之后的操作
TestLoader测试加载器：加载测试用例
TestRunner测试运行器：运行指定的测试用例

## unittest实例
单元测试：测试函数

`Q&A：为什么没有main方法也可以运行呢？`
unittest运行方式有两种：
1、命令行的运行方式(默认的测试用例运行方式)
    1)python -m unittest 文件名.py
    如：python -m unittest test_unittest.py
    2)python -m unittest 模块名.类名.函数名
    如：python -m unittest test_unittest.Tes
    tUnittest.test_02_combs
    注：python -m是以脚本（命令行）的方式来运行测试用例。
    3)python -m unittest -v 模块名.py
    注：-v(verbose)详细的，啰嗦的。
    4)python -m unittest -v 模块名.py -k *_combs
    注：-k通过通配符匹配方法名。
    
2、强制通过main运行
需要Edit Configurations手动添加要执行的.py文件，修改运行环境
unittest.main()

## unittest的测试用例运行结果
“.” 成功
“F” 失败
“E” 错误
“s” 用例跳过 
注：以上四种方式不能通过-v的方式运行

## unittest测试用例的执行顺序规则
以ASCII的编码大小排序【0-9，A-Z，a-z】
通过 ord('a')查看ASCII码

## 多种unittest的加载和运行测试用例的方式
1、main方法
2、通过测试套件来加载运行
`AddTest`
    _# 创建一个测试套件
    suite = unittest.TestSuite()
    # 通过测试套件加载测试用例
    suite.addTest(TestUnittest('test_01_todd'))
    suite.addTest(TestUnittest('test_02_combs'))
    # 运行时传入默认suite参数就可以指定执行
    unittest.main(defaultTest='suite')_
`AddTests`
_if __name__ == '__main__':
    # 创建一个测试套件
    suite = unittest.TestSuite()
    # 通过测试套件加载测试用例
    testcases = [TestUnittest('test_01_todd'), TestUnittest('test_02_combs')]
    suite.addTests(testcases)
    # 运行时传入默认suite参数就可以指定执行
    unittest.main(defaultTest='suite')_    
3、加载一个目录下的所有测试用例
_if __name__ == '__main__':
    # *.py是执行所有python文件里的测试用例，test_*.py是执行有test_前缀的文件里的测试用例
    suite = unittest.defaultTestLoader.discover('./demo', pattern='*.py')
    unittest.main(defaultTest='suite')_
    
`Q&A：为什么我们调用unittest.main()就可以执行测试用例`
需要了解unittest的main函数继承底层原理，main = TestProgram 而TestProgram的构造函数__init__包含很多参数，
_def __init__(self, module='__main__', defaultTest=None, argv=None,
                    testRunner=None, testLoader=loader.defaultTestLoader,
                    exit=True, verbosity=1, failfast=None, catchbreak=None,
                    buffer=None, warnings=None, *, tb_locals=False):_
其中各个参数的值分别为：
`module:`测试用例所在的路径，__main__表示当前路径
`defaultTest:`默认的待测试的测试用例的名称，默认执行所有用例
`argv:`接收外部传递给程序的外部参数
`testRiunner：`测试运行器
`testLoader：`测试加载器
`exit:` 是否在测试完成结束之后退出程序
`verbosity:`显示信息的详细程度。就是verbose -v。
数值<=0时只显示用例的总数和全局的执行结果。
数值1是默认值，显示用例总数和全局结果，并且对每个用例的结果有个标注。
“.” 成功
“F” 失败
“E” 错误
“s” 用例跳过 
数值>=2是显示用例总数和全局结果，并输出每个用例的详细结果
`failfast：`是否在测试用例失败时终止测试。

`测试夹具（固件，钩子函数，前后置）TestFixtrue详解`
setUp/tearDown 测试用例之前和之后
pytest:fixture  实现部分前置，差异化的前置
setUpClass/tearDownClass 测试类之前和之后（必须加@classmethod装饰器）
setUpModule，tearDownModule 测试模块之前和之后

`夹具封装：`
自动化测试框架必备的思想（有很多重复的代码），需要封装。

`忽略测试用例`


`自动化测试框架设计模式：`
1、POM设计模式：基础封装层，页面对象层，测试用例层。
2、关键字驱动模式：关键字封装

`公共的封装层：`
1、钩子函数封装
2、selenium二次封装
3、.ini文件和yaml全局配置文件封装
4、Excel/CSV文件的读写封装
5、数据库操作封装
6、调用外部的第三方库封装

`数据层：`
EXCEL数据驱动
CSV数据驱动
YAML数据驱动
数据库数据驱动

`文件层：`
1、HTML报告文件
2、Log日志文件
3、全局配置文件
4、错误截图文件
5、邮件附件文件
6、接口关联文件

`Github版本控制集成pycharm开发`
`Jenkins定时构建定时执行，持续集成`

`断言（判断用例是否执行成功）`
assertEqual(a,b)        a==b
assertNotEqual(a,b)     a!=b
assertTrue(x)           bool(x) is True
assertFalse(x)          bool(x) is False
assertIs(a,b)           a is b
assertIsNot(a,b)        a is not b
assertIsNotNone(x)      x is not None
assertIn(a,b)           a in b
assertNotIn(a,b)        a not in b
assertIsInstance(a,b)   isinstance(a,b)
assertNotIsInstance(a,b) not isinstance

`实际工作应用断言：`
assertEqual(a, b)
assertIn(a, b)
assertTrue(x)

`批量生成测试报告`