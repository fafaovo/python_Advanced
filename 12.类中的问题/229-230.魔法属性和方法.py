"""
# 魔术属性
__doc__ 获取类的描述信息
__modle__ 当前操作的对象在哪个模块
__class__ 当前操作的对象的类是什么
__dict__ 获取信息返回字典
# 魔术方法
__str__ 直接打印对象时
__del__ 当del的时候执行
__call__ 对象()时调用
"""


class goods(object):
    """这是一个商品的注释"""
    goods_color = '白色'  # 类属性

    def __init__(self):
        self.org_price = 100    # 实例属性

    def set_price(self):
        """这是goods类定义设置价格的方法"""
        pass

    def __call__(self, *args, **kwargs):
        print("__call__方法被调用")

    def __getitem__(self, item):
        # 对象在 对象['item'] 时调用
        print(f"getitem key = {item}")
        pass

    def __setitem__(self, key, value):
        # 对象在 对象['key'] = value 时调用
        print(f"setitem key = {key},value = {value}")
        pass

    def __delitem__(self, key):
        print(f"delitem key = {key}")
        pass


print(goods.__doc__)
print(goods.set_price.__doc__)
s = goods()
s()  # call方法被调用
print(s.__dict__) # 获取对象信息
print(goods.__dict__) # 获取类信息
print("--"*20)
s['a']
s['a'] = 10
del s['a']

