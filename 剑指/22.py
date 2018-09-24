# -*- coding:utf-8 -*-
class treeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        a=[]
        a.append(root)
        i=0
        while root:
            print(root.val)
            if root.left:
                a.append(root.left)
            if root.right:
                a.append(root.right)
            if i+1<len(a):
                i=i+1
                root=a[i]
            else:
                root=None


    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getBSTwithPreTin(self, pre, tin):
        if len(pre) == 0 | len(tin) == 0:
            return None
        root = treeNode(pre[0])
        for order, item in enumerate(tin):
            if root.val == item:
                root.left = self.getBSTwithPreTin(self,pre[1:order + 1], tin[:order])
                root.right = self.getBSTwithPreTin(self,pre[order + 1:], tin[order + 1:])
                return root

if __name__ == '__main__':
    s=Solution
    preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8]
    middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]
    treeRoot1 = s.getBSTwithPreTin(s,preorder_seq, middleorder_seq)
    s.PrintFromTopToBottom(s,treeRoot1)
