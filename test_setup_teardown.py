#类外测试
#python中一个模块就是一个文件。setup_module可实现整个模块中只执行一次
def setup_module():
    print("\n&&&setup_module : 整个模块中只执行一次")
def teardown_module():
    print("\n&&&teardown_module : 整个模块中只执行一次")
def setup_function():
    print("\nsetup_function : 每个不在类里面的用例开始前会执行")
def teardown_function():
    print("\nteardown_function : 每个不在类里面的用例结束后会执行")

def test_demo1():
    print("\nThis is test1")
def test_demo2():
    print("\nThis is test2")

#类内测试
class Test_all():
    def setup_class(self):
        print("\n###setup_class : class 类里面的所有用例执行前执行")
    def teardown_class(self):
        print("\n###teardown_class : class 类里面的所有用例执行后执行")
    def setup (self):
        print("\nsetup:每个用例开始前执行")
    def teardown (self):
        print("\nteardown:每个用例结束后执行")
    def test_demo3(self):
        print("\nThis is test3")
    def test_demo4(self):
        print("\nThis is test4")