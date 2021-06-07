# python提供了一个contextmanager的装饰器,简化上下文管理器
# 通过yield进行分割
"""
yieid生成器的作用
        1.可以充当return的作用
        2.能够保存程序的状态
"""
from contextlib import contextmanager

@contextmanager
def MyOpen(file_name, file_mode):
    print("上文")
    file = open(file_name, file_mode)
    yield file
    print("下文")
    file.close()
    pass


with MyOpen("hello.txt", "r") as file:
    result = file.read()
    print(result)
