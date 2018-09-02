# 题目描述
# 输入一个链表，反转链表后，输出新链表的表头。
import time
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        a = pHead
        h = pHead
        c = None
        while (a):
            h = a
            b = a.next
            a.next = c
            c = a
            a = b
        return h  #返回h，因为h是调整后的链表头，直接返回a，则a只是下一次的b，不一定能继续


        # if not pHead or not pHead.next:
        #     return pHead
        # else:
        #     newHead = self.ReverseList(self,pHead.next)
        #     pHead.next.next = pHead
        #     pHead.next = None
        #     return newHead

if __name__=='__main__':
    l1 = ListNode(1)
    l2 = ListNode(4)
    l1.next = l2
    l3 = ListNode(1)
    l2.next = l3
    l4 = ListNode(2)
    l3.next = l4
    l5 = ListNode(1)
    l4.next = l5
    l6 = ListNode(5)
    l5.next = l6
    l6.next = None
    s=Solution
    time1=time.time()
    a=s.ReverseList(s,l1)
    time2=time.time()
    print(time2-time1)
    print(a.val)