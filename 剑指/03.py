# 题目描述
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(listNode):
        # write code here
        a=[]
        while listNode:
            a.append(listNode.val)
            listNode = listNode.next

        return a[: :-1]


if __name__ == '__main__':
    # a=[1,2,3,4,5]
    # print(a[-2:-4:-1])  c:顺序为1 逆序为-1 a:从指定顺序开始的第几个开始 b:顺序为len 逆序为-(len+1)
    list1=ListNode(1)

    list2=ListNode(2)
    list1.next=list2

    list3=ListNode(3)
    list2.next = list3

    list4=ListNode(4)
    list3.next=list4
    list4.next=None
    a=Solution.printListFromTailToHead(list1)
    print(a)