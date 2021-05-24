"""
1.存在函数嵌套关系
2.内层函数引用了外层函数的变量
3.外层函数返回内层函数的地址
"""
"""
    def fun_a(m_a):
        def fun_b():
            print(m_a)
            # 内部定义的变量
            m_a = 80
            # 造成错误的原因：编译器认为内层函数已经定义了num变量，优先使用内部

        return fun_b
"""


def fun_a(m_a):
    def fun_b():
        nonlocal m_a
        # 告诉编译器这个m_a是外部变量
        print(m_a)
        m_a = 80
    return fun_b


b = fun_a(60)
b()
