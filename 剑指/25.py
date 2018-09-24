# 题目描述
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，
# 一个指向下一个节点，另一个特殊指针指向任意一个节点），
# 返回结果为复制后复杂链表的head。
# （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        a=pHead
        new=RandomListNode(a.label)
        new1=new
        while a.next:
            a=a.next
            head=RandomListNode(a.label)
            new.next=head
            new=new.next
        a=pHead
        new=new1
        while a.next:
            if a.random:
                new2=new1
                while new2:
                    if new2.label == a.random.label:
                        new.random = new2
                        break
                    new2=new2.next
            a=a.next
            new=new.next
        a=a


if __name__ == '__main__':
    r1=RandomListNode(1)
    r2 = RandomListNode(2)
    r1.next=r2

    r3 = RandomListNode(3)
    r2.next=r3
    r4 = RandomListNode(4)
    r3.next=r4
    r1.random=r4
    r5 = RandomListNode(5)
    r4.next=r5
    r6 = RandomListNode(6)
    r5.next=r6
    r7 = RandomListNode(7)
    r6.next=r7
    r7.next=None
    s=Solution
    s.Clone(s,r1)