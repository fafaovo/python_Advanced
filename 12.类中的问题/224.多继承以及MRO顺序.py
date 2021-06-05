# 参考C++菱形继承
# 菱形继承会让爷被孙继承多次
# 解决方法:super()


class Animal(object):
    def __init__(self, name='动物'):
        self.name = name
        print('动物初始化')


class Dove(Animal):
    def __init__(self, name='鸽子', Calls1='咕咕咕咕咕咕', *args, **kwargs):
        super(Dove, self).__init__(name)
        self.Calls1 = Calls1
        print('鸽子初始化')


class Frog(Animal):
    def __init__(self, name='青蛙', Calls2='孤寡孤寡孤寡', *args, **kwargs):
        super(Frog, self).__init__(name)
        self.Calls2 = Calls2
        print('青蛙初始化')


class Pigeon_frog(Frog, Dove):
    def __init__(self, Calls1, Calls2, name='咕鸽'):
        super().__init__(name, Calls1, Calls2)
        print('咕鸽初始化')


a = Pigeon_frog('咕咕', '孤寡')
for i in Pigeon_frog.mro():
    print(i)

# super继承方法是按照__mro__方法
