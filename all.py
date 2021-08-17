# 这是test_unittest.py, test_pytest.py相关的执行main文件
import os
import unittest
import pytest
from demo.test_unittest import TestUnittest

# if __name__ == '__main__':
#     # 创建一个测试套件
#     suite = unittest.TestSuite()
#     # 通过测试套件加载测试用例
#     testcases = [TestUnittest('test_01_todd'), TestUnittest('test_02_combs')]
#     suite.addTests(testcases)
#
#     # suite.addTest(TestUnittest('test_01_todd'))
#     # suite.addTest(TestUnittest('test_02_combs'))
#
#     # 运行时传入默认suite参数就可以指定执行
#     unittest.main(defaultTest='suite')
# 执行所有测试用例
if __name__ == '__main__':
    # *.py是执行所有python文件里的测试用例，test_*.py是执行有test_前缀的文件里的测试用例
    suite = unittest.defaultTestLoader.discover('./demo', pattern='*.py')
    unittest.main(defaultTest='suite')