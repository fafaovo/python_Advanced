def fun01(*args, **kwargs):
    print(args)
    print(kwargs)


def fun02(*args, **kwargs):
    # 此处没有进行拆包，导致参数传递不符合要求
    # fun01(args, kwargs)
    # 所以需要拆一下包
    fun01(*args, **kwargs)

if __name__ == '__main__':
    fun01(10, 20, 30, a=10, b=20)
    fun02(10, 20, 30, a=10, b=20)
