"""
生成器generator是一个特殊的迭代器
(保存位置,返回下一个值)
next(生成器) 也能得到下一个值
"""

"""列表推导式"""
data_list1 = [i * 2 for i in range(10)]
print(data_list1)

"""这就是生成器的创建1"""
data_list2 = (i * 2 for i in range(10))
print("---->", next(data_list2))
print("---->", next(data_list2))
"""生成器的第二种方式"""
# 这是一个函数
def test():
    return 10
m = test()
print(m)
"""第二种方式 使用yield创建了一个生成器"""
def test1():
    yield 10
n = test1()
print(f"---->{next(n)}")
