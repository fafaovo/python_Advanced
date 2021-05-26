def fun_out(func):
    def fun_in(num):
        print("开始验证")
        func(num)

    return fun_in


# 登录函数
@fun_out
def login(num):
    print(f"开始登录 = {num}")


login(10)
