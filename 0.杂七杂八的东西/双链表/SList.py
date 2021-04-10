class SListNode(object):
    def __init__(self, SNext, SPrev, Data):
        self.SNext = SNext
        self.SPrev = SPrev
        self.Data = Data


class SList(object):
    def HeadAdd(self, listHead, data):
        newNode = SListNode(listHead.SNext, listHead, data)
        listHeadNext = listHead.SNext
        listHead.SNext = newNode
        listHeadNext.SPrev = newNode
        pass

    def HeadRemove(self, listHead):
        if listHead.SNext == listHead:
            return
        cur = listHead.SNext
        listHead.SNext = cur.SNext
        cur.SNext.SPrev = listHead
        del cur

    def FooterAdd(self, listHead, data):
        newNode = SListNode(listHead, listHead.SPrev, data)
        listHead.SPrev.SNext = newNode
        listHead.SPrev = newNode
        pass

    def FooterRemove(self, listHead):
        if listHead.SPrev == listHead:
            return
        cur = listHead.SPrev
        cur.SPrev.SNext = listHead
        listHead.SPrev = cur.SPrev
        del cur
        pass

    def print(self, phead):
        if phead.SNext == phead:
            print("链表无元素")
            return
        cur = phead.SNext
        print("head", end="->")
        while cur.SNext != phead:
            print(cur.Data, end="->")
            cur = cur.SNext
        print(cur.Data)


def SListinit():
    headNode = SListNode(None, None, 0)
    headNode.SNext = headNode
    headNode.SPrev = headNode
    return headNode


def text1():
    ovo = SListinit()
    slb = SList()
    slb.HeadAdd(ovo, 3)
    slb.HeadAdd(ovo, 2)
    slb.HeadAdd(ovo, 1)
    slb.print(ovo)
    slb.HeadRemove(ovo)
    slb.HeadRemove(ovo)
    slb.HeadRemove(ovo)
    slb.print(ovo)
    slb.FooterAdd(ovo, 1)
    slb.FooterAdd(ovo, 2)
    slb.FooterAdd(ovo, 3)
    slb.print(ovo)
    slb.FooterRemove(ovo)
    slb.FooterRemove(ovo)
    slb.FooterRemove(ovo)
    slb.print(ovo)


def main():
    text1()


if __name__ == '__main__':
    main()
