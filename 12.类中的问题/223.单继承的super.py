class Parent(object):
    def __init__(self, name):
        self.name = name
        print('parent的init结束调用')


class son1(Parent):
    def __init__(self, name, age):
        self.age = age
        super(son1, self).__init__(name)
        print('son的init结束调用')


class Grandson(son1):
    def __init__(self, name, age, gender):
        self.gender = "男"
        super(Grandson, self).__init__(name, age)
        print('Grandson的init结束调用')


gs = Grandson('grandson', 17, '男')
for i in Grandson.__mro__:
    print(i)
# parent -> son1 ->grandson
# 等同于C++中的继承
"""
super的调用和使用
"""