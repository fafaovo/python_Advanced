"""
此处的可变和不可变指的是内存中的那一块区域是否可以被改变
可变类型：创建后可以继续修改对象的内容 [字典 列表]
不可变类型：一旦创建就不可修改的对象 [数字 字符串 元组]

可变，可以扩张的内存
不可变.需要扩张时重新开辟一块空间 然后释放之前的空间
"""


def test():
    # 列表是一个不可变类型
    a = 5
    print(f"a = {id(a)}")
    # 修改变量 重新开辟一块内存空间存放a的值
    a = 5 + 1
    print(f"a = {id(a)}")


# 列表是一个可变类型
list = [1, 3, 5]
print(f"{list} = ,{id(list)}")

list.append(7)
print(f"{list} = ,{id(list)}")

list1 = list
list1.append(9)
print(f"{list} = ,{id(list)}")