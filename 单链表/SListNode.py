"""
用python写个单链表的 增 删 查 改 排序
头插 头删 尾插 尾删
"""


class listNode(object):
    def __init__(self, data, nextNode):
        self.data = data
        self.next = nextNode
    pass


class ListNodeFunction(object):
    def __init__(self):
        self.__head = None

    def headAdd(self, elem):
        """头插"""
        newNode = listNode(elem, self.__head)
        self.__head = newNode
        """新建一个节点把值和头节点传进去,然后再把新节点赋给头"""

    def headRemove(self):
        """头删"""
        if self.__head is not None:
            """当头不等于None时"""
            cur = self.__head.next
            """将cur给到头节点的下一个节点"""
            del self.__head
            """删除头节点"""
            self.__head = cur
            """将头节点的下一个节点赋给头节点"""
        else:
            print("没有元素可以删除")

    def footerAdd(self, elem):
        """尾插"""
        cur = self.__head
        """将头节点给cur"""
        newNode = listNode(elem, None)
        """新建节点，因为在尾部，所以第二个参数直接传None"""
        if self.__head is None:
            """当整个链表为空时 将新建的节点直接给到头节点"""
            self.__head = newNode
            return
        while cur.next is not None:
            """遍历整个单链表,找到cur.next == None的数 此时cur就指向单链表中的最后一个元素"""
            cur = cur.next
            """遍历数组的条件"""
        else:
            """如果循环结束，则把新建的节点给到最后一个元素的next"""
            cur.next = newNode

    def footerRemove(self):
        """尾删"""
        if self.__head is None:
            """第一种情况 当尾部就是None时"""
            print("没有可删除的元素")
            return
        elif self.__head.next is None:
            """第二种情况 当尾部的下一个就是None时"""
            del self.__head
            self.__head = None
            return
        else:
            """第三种情况 正常链表"""
            cur = self.__head
            pos = None
            while cur.next is not None:
                pos = cur
                cur = cur.next
            else:
                del cur
                pos.next = None
            return

    def seek(self, elem):
        """链表查找"""
        cur = self.__head
        count = 0
        while cur is not None:
            if cur.data == elem:
                print(f"你要查找的{elem}找到了,是第{count}个元素")
                return
            else:
                cur = cur.next
                count += 1
        else:
            print("找不到")

    def appointAdd(self, pos, elem):
        """pos->位置 elem->要插入的元素 指定位置插入"""
        cur = self.__head
        zero = None
        count = 1
        while cur is not None:
            if count == pos:
                newNode = listNode(elem, cur)
                if pos == 1:
                    """当pos位置为1时,即头插"""
                    self.__head = newNode
                    return
                zero.next = newNode
                return
            else:
                zero = cur
                count += 1
                cur = cur.next
        else:
            if count < pos:
                print("位置过大")
            elif count == pos:
                """当元素个数等于插入位置时,即尾插"""
                newNode = listNode(elem, None)
                zero.next = newNode
        pass

    def appointRemove(self, pos):
        """指定位置删除"""
        if self.__head is None:
            print("没有可删除的内容")
            return
        else:
            count = 1
            cur = self.__head
            zero = None
            while cur is not None:
                if pos == count:
                    if pos == 0:
                        """当pos为0时候，即为头删"""
                        del self.__head
                        self.__head = cur.next
                        return
                    else:
                        zero.next = cur.next
                        del cur
                        return
                else:
                    if (cur.next is None) and (pos == count):
                        """当cur.next为None pos==count时，进行尾删"""
                        zero.next = None
                        del cur
                        return
                    count += 1
                    zero = cur
                    cur = cur.next
            else:
                """此时cur == None"""
                print("你要删除元素的pos过大")
        pass

    def print(self):
        """遍历并且打印"""
        cur = self.__head
        while cur is not None:
            print(cur.data, end="->")
            cur = cur.next
        else:
            print("none")
        pass

    def modify(self, elem, newElem):
        """修改元素"""
        cur = self.__head
        while cur is not None:
            if cur.data is elem:
                cur.data = newElem
            else:
                cur = cur.next
        else:
            print("没找到你输入")
        pass

    def sort(self):
        """排序链表的元素"""
        sortHead = self.__head
        """新元素的头"""
        cur = self.__head.next
        """下一个元素"""
        sortHead.next = None
        """将新元素的下一个指向None"""
        while cur is not None:
            curNext = cur.next
            if cur.data <= sortHead.data:
                """进来进行第一次判断是否进行头插"""
                cur.next = sortHead
                sortHead = cur
            else:
                """因为不可能是头插，所以只有中间插入和尾插的可能性"""
                sortPrev = sortHead
                sortCur = sortHead.next
                while sortCur is not None:
                    if cur.data <= sortCur.data:
                        sortPrev.next = cur
                        cur.next = sortCur
                        break
                    else:
                        sortPrev = sortCur
                        sortCur = sortPrev.next
                if sortCur is None:
                    sortPrev.next = cur
                    cur.next = None
            cur = curNext
        self.__head = sortHead
        pass


if __name__ == '__main__':
    """创建一个单链表"""
    LN = ListNodeFunction()
    """对于单链表进行的测试"""
    i = 5
    while i:
        LN.headAdd(i)
        i -= 1
    LN.print()
    for i in range(5):
        LN.headRemove()
    LN.print()
    for i in range(5):
        LN.footerAdd(i)
    LN.print()
    """
    for i in range(5):
        LN.footerRemove()
    LN.print()
    """
    LN.seek(4)
    LN.modify(4, 8)
    LN.print()
    LN.appointAdd(2, 6)
    LN.print()
    LN.appointAdd(6, 9)
    LN.print()
    LN.appointRemove(2)
    LN.print()
    LN.appointRemove(0)
    LN.print()
    LN.appointRemove(5)
    LN.print()
    LN.appointRemove(2)
    LN.print()
    LN.appointAdd(2, 4)
    LN.print()
    LN.sort()
    LN.print()


