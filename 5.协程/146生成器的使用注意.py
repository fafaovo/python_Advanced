"""
在生成器中
使用return会让生成器结束 并且捕获异常时候可以捕获到return返回的内容

"""


def MyFibnacci(n):
    m_a = 1
    m_b = 1
    m_index = 0
    while not m_index == n:
        data = m_a
        m_a, m_b = m_b, m_a + m_b
        m_index += 1
        print("该状态已暂停")
        xxx = yield data
        print("该状态已执行")

        if xxx == 1:
            return "我可以让生成器结束"
        """
        yieid的作用 
        yieid可以让程序暂停执行并且，并且保存程序暂停执行的状态
        1.可以充当return的作用
        2.能够保存程序的状态 
        """


if __name__ == '__main__':
    fib = MyFibnacci(5)

    value = next(fib)
    print("第一列", value)

    value = next(fib)
    print("第二列", value)

    try:
        value = fib.send(1)
        # send和next一样会唤醒编译器 此处的1会传递到xxx
        print("第三列", value)
    except Exception as i:
        print(i)
