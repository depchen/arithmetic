# 题目描述
# 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
# (注意: 在返回值的list中，数组长度大的数组靠前)
# -*- coding:utf-8 -*-
class treeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        result = []
        if root ==None:
            return result
        if root.right == None and root.left== None and root.val==expectNumber:
            return [[root.val]]
        else:
            letf=self.FindPath(self,root.left,expectNumber-root.val)
            right=self.FindPath(self,root.right,expectNumber-root.val)
            for i in letf+right:
                result.append([root.val]+i)
            return result

    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getBSTwithPreTin(self, pre, tin):
        if len(pre) == 0 | len(tin) == 0:
            return None
        root = treeNode(pre[0])
        for order, item in enumerate(tin):
            if root.val == item:
                root.left = self.getBSTwithPreTin(self, pre[1:order + 1], tin[:order])
                root.right = self.getBSTwithPreTin(self, pre[order + 1:], tin[order + 1:])
                return root

if __name__ == '__main__':
    s = Solution
    preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8]
    middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]
    treeRoot1 = s.getBSTwithPreTin(s, preorder_seq, middleorder_seq)
    a=s.FindPath(s, treeRoot1,9)
    print(a)