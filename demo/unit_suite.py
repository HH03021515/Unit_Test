# author:ToddCombs  测试套件

from demo.unit_test_openfile import *

# 创建一个测试套件 == list
suite = unittest.TestSuite()

# 引入测试用例到测试套件
suite.addTest(forTestTest('test_4'))
suite.addTest(forTestTest('test_3'))
suite.addTest(forTestTest('test_5'))

# 套件通过TextTestRunner对象进行运行， ≈ unittest.main()
# unittest.main()运行所有内容，而TextTestRunner仅运行选中的用例
runner = unittest.TextTestRunner()
runner.run(suite)