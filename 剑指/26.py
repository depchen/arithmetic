# 题目描述
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self,root, val):
        if root is None:
            root = TreeNode(val);
        else:
            if val < root.val:
                root.left = self.insert(root.left, val);  # 递归地插入元素
            elif val > root.val:
                root.right = self.insert(root.right, val);
        return root;

class Solution:
    def __init__(self):
        self.l=None
        self.r=None

    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None
        self.Convert(pRootOfTree.left)
        if self.l==None:
            self.l=pRootOfTree
            self.r=pRootOfTree
        else:
            self.r.right=pRootOfTree
            pRootOfTree.left=self.r

            self.r=pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.l

def printList(head):
    while head.right:
        print(head.val, end=" ")
        head = head.right
    print(head.val)
    while head:
        print(head.val, end=" ")
        head = head.left


if __name__ == '__main__':
    t=TreeNode(6)
    t.insert(t,1)
    t.insert(t,2)
    t.insert(t,4)
    t.insert(t,7)
    t.insert(t,8)
    s=Solution()
    a=s.Convert(t)
    printList(a)
