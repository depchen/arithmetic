# -*- coding:utf-8 -*-
# 题目描述
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
# 则重建二叉树并返回。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            res = TreeNode(pre[0])
            res.left = self.reConstructBinaryTree(self,pre[1:tin.index(pre[0])+1],tin[0:tin.index(pre[0])])
            res.right = self.reConstructBinaryTree(self,pre[tin.index(pre[0])+1:],tin[tin.index(pre[0])+1:])
        return res

if __name__ == '__main__':
    a=[1,2,4,7,3,5,6,8]
    b=[4,7,2,1,5,3,8,6]
    solu=Solution
    res=solu.reConstructBinaryTree(solu,a,b)
    a=0
