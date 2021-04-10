"""
斐波那契数列：从第三个开始，后续数字等于前两个之和
1 1 2 3 5 8 13

公式: a=1 b=1 然后 a=b b=a+b 最终保留a的值输出
"""


class MyFibnacci(object):
    def __init__(self, IterMax):
        self.m_index = 0
        self.IterMax = IterMax
        self.m_a = 1
        self.m_b = 1

    def __iter__(self):
        """迭代器通常返回自己"""
        """
        for循环检测的是一个可迭代对象，
        迭代器本身满足可迭代对象的全部要求
        所以说他本身也是个可迭代对象
        主要是__iter__返回了本身
        """
        return self
        pass

    def __next__(self):
        if self.m_index == self.IterMax:
            raise StopIteration
        else:
            next_a = self.m_a
            self.m_a = self.m_b
            self.m_b = next_a + self.m_b
            """
            也可以写成
            self.m_a ,self.m_b = self.m_b ,self.m_a + self.m_b
            交换变量
            """
            self.m_index += 1
            return next_a


"""
来整理一下这里的思路，第一次迭代时，a和b的值不变
当第二次进来的时候，a = b 然后此时 b = 还没赋值前的a + b
因为前面已经改变了a 所以需要这个额外的变量next_a来存储还没改变的a
最后返回一开始保存a的值

"""

if __name__ == '__main__':

    for i in MyFibnacci(20):
        print(i, end=" ")
