class Foo(object):
    # @property
    def get_bar(self):
        return 'laotie'

    # 类属性 property产生了个对象
    # property()
    # 第一个参数 foo.BAR 自动调用第一个参数的方法
    # 第二个参数 foo.BAR = 100 会调用第二个方法
    # 第三个参数 del foo.BAR 会调用第三个方法
    # 第四个参数 foo.BAR.__dic__ 会调用第四个方法
    # __dic__ 帮助方法
    BAR = property(get_bar)


foo = Foo()
# print(foo.get_bar)
print(foo.BAR)
print("-"*30)


class goods(object):
    def __init__(self):
        self.org_price = 1000
        self.discount = 0.7
        # 原价和折扣

    def get_price(self):
        return self.org_price * self.discount

    def set_price(self, val):
        self.org_price = val
        print('set_price')

    def del_price(self):
        print("执行了 deleter 方法")

    BAR = property(get_price, set_price, del_price, "这是一个测试")


if __name__ == '__main__':
    S = goods()
    print(S.BAR)
    S.BAR = 100
    del S.BAR
    print(S.BAR.__doc__)
