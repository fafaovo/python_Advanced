# 在装饰器外套一个函数，即为装饰器工厂
def test(path):
    print(path)
    def fun_out(func):
        def fun_in(num):
            print(f"{num}验证中")
            func(num)
        return fun_in
    return fun_out

@test("login.py")
def login(num):
    print(f"{num}登录中")
# test("login.py") 可以分解为两步 有参数的情况下
# 1 test("login.py")
# 2. @ 第一步的结果
"""定义不会执行，然后就返回了fun_out 然后就变成了@fun_out"""
login(1)