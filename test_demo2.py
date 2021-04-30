import pytest
class Test_demo2():
    @pytest.mark.test1
    def test_demo1(self):
        a = 5
        b = -1
        assert a != b
        print("测试1成功！！！")
    @pytest.mark.test2
    def test_demo2(self):
        a = 5
        b = -1
        assert a == b
        print("测试2成功！！！")