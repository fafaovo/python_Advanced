from collections.abc import Iterable

"""
我们在迭代一个可迭代的对象时，实际上就是先获取该对象提供的迭代器
然后通过这个迭代器来依次获取对象中的每一个数据

获取对象的迭代器 iter(可迭代对象)
next(迭代器)可以获取下一个元素
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
"""判断是否可迭代"""
if isinstance(list1, Iterable):
    """获取迭代器"""
    iterator = iter(list1)
    """迭代下一个对象"""
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

"""
迭代器特定：
1.记录遍历位置 2.获取下一个元素的地址

自定义迭代器:
1.必须包含__iter__()
2.必须包含__next__()
当有这两个方法的时候这个类可以称为迭代器的类
"""


class MyIterator(object):
    def __iter__(self):
        pass

    """当next()时候会自动调用这个方法"""
    def __next__(self):
        pass
