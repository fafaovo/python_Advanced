class MyList(object):
    def __init__(self):
        """初始化"""
        self.item = []
        pass

    def __iter__(self):
        """迭代器"""
        myiter = MyIter(self.item)
        return myiter
        pass

    def AddItem(self, node):
        self.item.append(node)
        pass


class MyIter(object):
    def __init__(self, item):
        self.item = item
        self.index = 0
        pass

    def __iter__(self):
        pass

    def __next__(self):
        if self.index < len(self.item):
            data = self.item[self.index]
            self.index += 1
            return data
        else:
            raise StopIteration


if __name__ == '__main__':
    mylist = MyList()
    mylist.AddItem(1)
    mylist.AddItem(3)
    mylist.AddItem(7)
    mylist.AddItem(9)
    for i in mylist:
        print(i)
