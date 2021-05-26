def fun_out(func):
    def fun_in(*args, **kwargs):  # 带参数的传递在这里
        print("正在验证")
        func(*args, **kwargs)     # 带参数的传递在这里

    return fun_in


@fun_out
def login(*args, **kwargs):  # 带参数的传递在这里
    print(f"开始登录")
    print(f"login:args={args}")
    print(f"login:kwargs={kwargs}")


login(10, a=10)
