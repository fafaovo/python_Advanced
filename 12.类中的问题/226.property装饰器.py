# @property[婆婆提] 可以简化我们对一个对象的属性的操作
class Foo(object):
    def __init__(self,num):
        self.num = num

    # 特殊装饰器装饰方法
    @property
    def prop(self):
        return self.num


foo = Foo(100)
# print(foo.prop())
# 省....了个括号
print(foo.prop)
