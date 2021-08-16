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

Q&A：为什么没有main方法也可以运行呢？
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


