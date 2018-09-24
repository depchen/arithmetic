# 题目描述
#二叉搜索树 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
# 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
# 它的左、右子树也分别为二叉排序树。
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.flag=False
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) < 0:
            return False
        if self.flag and len(sequence) == 0:
            return True
        if not self.flag and len(sequence) == 0:
            return False
        if min(sequence)>sequence[-1] or max(sequence)<sequence[-1]:
            return True

        index=0
        for i in range(len(sequence)-1):
            if sequence[i] >=sequence[-1]:
                break
            index = i
        for j in range(index+1,len(sequence)-1):
            if sequence[j]<sequence[-1]:
                return False
        left=True
        right=True
        self.flag=True
        if index>0:
            a = sequence[:index+1]
            left=self.VerifySquenceOfBST(sequence[:index+1])

        if index<len(sequence)-1:
            aa=sequence[index+1:len(sequence)-1]
            right = self.VerifySquenceOfBST(sequence[index+1:len(sequence)-1])
        return left&right


if __name__ == '__main__':
    s=Solution()
    a=[4,8,6,12,16,14,10]
    aa=s.VerifySquenceOfBST(a)
    print(aa)
