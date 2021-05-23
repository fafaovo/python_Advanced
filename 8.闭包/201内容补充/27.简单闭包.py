# 在一个外函数中定义了一个内函数,内函数运用了外函数的临时变量,并且外函数的返回值是内函数的引用,这样就构成了一个闭包
# 说白就是def a里面有个def b,但是def a的返回值是def b的地址


def fun_out(num):
    """这就是个闭包"""
    print(f"fun_out---num:{num}")

    def fun_in(num_in):
        print(f"fun_in---num:{num}")
        print(f"fun_in---num_in:{num_in}")

    return fun_in


fun_out(10)
# fun_out---num:10
test = fun_out(10)
test(20)
# fun_out---num:10
# fun_in---num:10
# fun_in---num_in:20
