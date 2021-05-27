# 函数前增加多个装饰器
def makeBold(func):
    def fun_in():
        return "<b>" + func() + "</b>"

    return fun_in


def makeItalic(func):
    def fun_in():
        return "<i>" + func() + "</i>"

    return fun_in


@makeBold  # test = makeBold(test)
@makeItalic  # test = makeBold(makeItalic(test))
def test():
    return "hello world-1"


# test = makeBold(makeItalic(test))
print(test())
