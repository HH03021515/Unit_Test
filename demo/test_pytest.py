# pytest 不用继承
import pytest

class TestPytest:

    def test_01_todd(self):
        print("测试todd")


if __name__ == '__main__':
    pytest.main()