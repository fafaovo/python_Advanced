class goods(object):
    def __init__(self):
        self.org_price = 1000
        self.discount = 0.7
        # 原价和折扣

    @property
    def price(self):
        return self.org_price * self.discount

    @price.setter
    def price(self, val):
        self.org_price = val

    @price.deleter
    def price(self):
        print("执行了 deleter 方法")


car = goods()
print(car.price)
car.price = 500  # car.price = 500 等同于 car.price(500)
print(car.price)

del car.price