"""
1.mylist类
初始化方法
__iter__()方法 对外提供迭代器
addItem() 方法 添加数据

2.自定义迭代器类 MylistIterator
初始化方法
迭代器方法 __iter__()
获取下一个元素值的方法__next__()

"""


# 1.mylist类
class MyList(object):
    # 初始化方法
    def __init__(self):
        # 定义实例属性，保存数据
        self.items = []
        pass

    # __iter__()方法 对外提供迭代器
    def __iter__(self):
        # 这么迭代呢？返回一个迭代器咯
        # 创建迭代器对象
        mylist_iterator = MylistIterator(self.items)
        return mylist_iterator
        pass

    # addItem() 方法 添加数据
    def addItem(self, data):
        # 追加数据
        self.items.append(data)
        pass


# 2.自定义迭代器类 MylistIterator
class MylistIterator(object):
    # 初始化方法
    def __init__(self, items):
        self.items = items
        """记录迭代器迭代的位置"""
        self.index = 0
        pass

    # 迭代器方法 __iter__()
    def __iter__(self):
        pass

    # 获取下一个元素值的方法__next__()
    # 当next（迭代器）的时候就会调用这个方法
    def __next__(self):
        # 1.判断当前下标是否越界，越界抛出异常
        # 每次进来时候先判断记录迭代器的指针是否小于数组长度
        # 如果大于或者等于就说明越界了
        # 2.获取下标对应的元素值，下标位置+1
        # 3.返回下标对应的数据
        if self.index < len(self.items):
            data = self.items[self.index]
            self.index += 1
            return data
        else:
            # 当下标越界的时候主动抛出异常
            # StopIteration 在迭代器下标越界时候会出现的异常
            raise StopIteration

        pass


if __name__ == '__main__':
    mylist = MyList()
    # 把列表传参
    mylist.addItem("张三")
    mylist.addItem("李四")
    mylist.addItem("王五")
    mylist.addItem("老六")
    mylist.addItem("小柒")
    mylist.addItem("王八")
    # 遍历
    # for循环的本质
    # 1.iter(mylist) 获取mylist对象的迭代器
    # 返回了一个迭代器 所以就获取到了迭代器
    # 2.next(迭代器) 获取下一个值
    # 3.捕获异常
    for value in mylist:
        print(value)

