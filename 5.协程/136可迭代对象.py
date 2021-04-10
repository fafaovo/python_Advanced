from collections.abc import Iterable

# python 3.8需要使用 collections.abc 模块

"""
迭代器->生成器->协程

可迭代对象: 可遍历对象 （列表 字符串 元组 字典 range()）

isinstance(待检测的对象, Iterable) 检测是否是可迭代对象 True 可迭代对象 False 不可迭代对象
可迭代对象的本质：对象所属的类中包含了__iter__()[一个迭代器] 方法
"""
listed = [1, 2, 3, 4, 5, 6]
ret = isinstance(listed, Iterable)
print(ret)

ret = isinstance(100, Iterable)
print(ret)


# 我们知道对象也是不可迭代的，但是可以增加一个方法
class MyClass(object):
    def __iter__(self):
        """魔术方法 增加一个__iter__方法"""
        """该方法就是个迭代器"""

    pass


myclass = MyClass()
print(isinstance(myclass, Iterable))
