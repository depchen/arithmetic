# 题目描述
# 输入一个链表，输出该链表中倒数第k个结点。
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(head, k):
        # write code here
        if head == None:
            return None
        else:
            n = []
            n.append(head)
            while (head.next):
                n.append(head.next)
                head = head.next
            if k > len(n):
                return None
            elif k == 0:
                return None
            else:
                return n[len(n) - k]

if __name__ == '__main__':
    l1=ListNode(1)
    l2=ListNode(4)
    l1.next=l2
    l3 = ListNode(1)
    l2.next=l3
    l4 = ListNode(2)
    l3.next=l4
    l5 = ListNode(1)
    l4.next=l5
    l6 = ListNode(5)
    l5.next=l6
    l6.next=None
    a=Solution.FindKthToTail(l1,1)
    print(a)