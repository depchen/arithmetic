# 题目描述
# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
# -*- coding:utf-8 -*-
class treeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 is None or pRoot2 is None:
            return False
        result = False
        if pRoot1.val == pRoot2.val:
            result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
        if result == False:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if result == False:
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def DoesTree1HaveTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot2.val != pRoot1.val:
            return False
        return self.DoesTree1HaveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HaveTree2(pRoot1.right, pRoot2.right)

    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getBSTwithPreTin(self, pre, tin):
        if len(pre)==0 | len(tin)==0:
            return None

        root = treeNode(pre[0])
        for order,item in enumerate(tin):
            if root .val == item:
                root.left = self.getBSTwithPreTin(pre[1:order+1], tin[:order])
                root.right = self.getBSTwithPreTin(pre[order+1:], tin[order+1:])
                return root


if __name__=='__main__':
    solution = Solution()
    preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8]
    middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]
    treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    preorder_seq = [1, 2, 3]
    middleorder_seq = [2, 1, 3]
    treeRoot2 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    a=solution.HasSubtree(treeRoot1, treeRoot2)
    print(a)