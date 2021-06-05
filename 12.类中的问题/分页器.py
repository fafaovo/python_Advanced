class Pager(object):
    def __init__(self, pages):
        self.pages = pages
        self.items = 10

    @property
    def m_prev(self):
        val = self.pages * self.items
        return val

    @property
    def m_next(self):
        val = (self.pages-1) * self.items + 1
        return val

book = Pager(14)
print(f"从{book.m_next}显示到{book.m_prev}")
