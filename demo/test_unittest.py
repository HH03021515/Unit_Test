# 简单的unittest实例
import unittest

class TestUnittest(unittest.TestCase):

    def test_01_todd(self):
        print("测试todd")

    def test_02_combs(self):
        print("测试combs")
        self.assertEqual(1, 2)

    def test_03_fraulen(self):
        print("测试fraulen")
        raise Exception("粗……粗错啦！")

    # 跳过用例
    @unittest.skip('这里可以输入跳过原因')
    def test_04_shen(self):
        print("测试shen")



if __name__ == '__main__':
    print("*********************")
    unittest.main()