def fun_out(func):
    def fun_in(num):
        print("开始验证")
        return func(num)

    return fun_in


@fun_out
def login(num):
    print(f"开始登录{num}")
    return num + 100


result = login(123)
print(result)


