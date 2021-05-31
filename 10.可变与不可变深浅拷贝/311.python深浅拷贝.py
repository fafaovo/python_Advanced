"""
浅拷贝
引用地址拷贝 并没有产生新的空间
如果拷贝内容是对象 对对象和copy对象都指向同一块内存空间
只拷贝父对象,不会拷贝对象的内部的子对象
深拷贝
源对象和copy对象都指向不同的内存空间
拷贝对象会拷贝子对象

针对可变对象 深浅拷贝都会产生一个新的空间
copy()浅拷贝
deepcopy()深拷贝
"""
import copy
list1 = [1,2,3]
print(f"{list1} = {id(list1)}")

list2 = copy.copy(list1)
print(f"{list2} = {id(list2)}")

