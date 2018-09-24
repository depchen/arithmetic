# 题目描述
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        #本题首先考虑两个链表是否为空，之后思路是两个指针比较，谁大谁不动的原则
        #注意的点是，可能会插入到头部，建立新的pHead1.
        #最后若不为空，还要链接
        a=pHead1
        aa=None
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        while a and pHead2:
            #两个队列比较 ，谁大谁的指针不动
            if a.x<pHead2.x:
                aa=a
                a=a.next
            else:
                #p=a.next
                if aa == None:
                    b = pHead2.next
                    pHead2.next=a
                    a=pHead2
                    pHead1=a
                    pHead2 = b
                else:
                    aa.next = pHead2
                    b=pHead2.next
                    pHead2.next=a
                    pHead2=b
        if a == None:
            aa.next=pHead2
        return pHead1



if __name__=='__main__':
    l1 = ListNode(1)
    l2 = ListNode(3)
    l1.next = l2
    l3 = ListNode(5)
    l2.next = l3
    # l4 = ListNode(4)
    # l3.next = l4
    # l5 = ListNode(5)
    # l4.next = l5
    # l6 = ListNode(5)
    # l5.next = l6
    l3.next = None

    m1 = ListNode(1)
    m2 = ListNode(3)
    m1.next = m2
    m3 = ListNode(5)
    m2.next = m3
    # m4 = ListNode(6)
    # m3.next = m4
    # m5 = ListNode(6)
    # m4.next = m5
    # m6 = ListNode(7)
    # m5.next = m6
    m3.next = None

    s=Solution
    pp=s.Merge(s,l1,m1)
    a=1