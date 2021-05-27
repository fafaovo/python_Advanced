class MyClass(object):
    def __init__(self, func):
        print("__init__方法")
        print(f"__func__{func}")
        self.func = func

    def run(self):
        print("奔跑中")
    """call 让类实例具备函数调用的特性"""

    def __call__(self, *args, **kwargs):
        print("开始call验证")
        # 调用原来login的内容
        self.func()


# a = MyClass()
# print(a)

# 对象其实也是个地址，但是需要使用魔术方法__call__才能让他变成一个函数
# a()


@MyClass
# login = MyClass(login)
def login():
    print("开始登录....")
"""
__init__方法，创建类时默认调用
login = MyClass(login)
此处的login 会传递到func中
"""
login()
