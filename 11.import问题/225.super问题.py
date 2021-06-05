class a(object):
    def __init__(self):
        print("a")


class b(a):
    def __init__(self):
        a.__init__(self)
        # super().__init__()
        print("b")


class c(a):
    def __init__(self):
        a.__init__(self)
        # super().__init__()
        print("c")


class d(b, c):
    def __init__(self):
        super().__init__()
        print("d")


D = d()
