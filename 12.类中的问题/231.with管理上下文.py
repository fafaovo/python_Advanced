# with管理上下文 但凡有上下文需要结合的需求可以用with改进
# 这是一段必出错的打开文件
# try:
#     with open('1.txt', 'r') as f:
# 此处的open('1.txt','r') as f 中的 f其实是 f = open('1.txt','r')
#         f.write("xxxx")
# except Exception as e:
#     print(f"文件操作错误{e}")
# 自定义类也可以实现这个规则
"""
上下文管理器
拿打开文件举例 打开文件[上文] 操作文件 关闭文件[下文]
"""
"""上下文管理器必须包含__enter__()和__exit__()方法"""


class MyFile(object):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode
        pass

    def __enter__(self):
        print("进入上文")
        self.file = open(self.file_name, self.file_mode)
        return self.file
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("进入下文")
        self.file.close()
        pass


if __name__ == '__main__':
    with MyFile("hello.txt", "r") as file:
        result = file.read()
        print(result)
