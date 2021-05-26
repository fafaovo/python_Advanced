# 装饰器通用版
def fun_out(func):
    def fun_in(*args, **kwargs):
        print("----这里可以添加新的内容----")
        return func(*args, **kwargs)
    return fun_in
