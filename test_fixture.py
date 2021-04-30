import pytest
# fixture类似setup和teardown，但是我们可以自定义测试用例的前置条件，并且可以跨文件使用
# fixture可以写在文件conftest.py文件里面
# @pytest.fixture()
# def myfixture1():
#     print("执行myfixture1")
class Test_firstFile():
    def test_one(self):
        print("执行test_one")
        assert 2 * 3 == 6
    def test_two(self,myfixture1):
        print("执行test_two")
        assert 2 - 5 == -3
    def test_three(self,myfixture1):
        print("执行test_three")
        assert 2 + 3 == 5