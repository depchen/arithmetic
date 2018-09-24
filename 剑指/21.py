# 题目描述
# 输入两个整数序列，第一个序列表示栈的压入顺序，
# 请判断第二个序列是否可能为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序，
# 序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        j=0
        pushv=[]
        for i in range(len(pushV)):
            pushv.append(pushV[i])
            a=i
            while j<len(popV) and pushv[-1]==popV[j]:
                pushv.pop()
                j=j+1
                a=a-1
        if pushv == []:
            return True
        else:
            return False


if __name__ == '__main__':
    s=Solution
    aa=[1,2,3,4,5]
    aa1=[4,5,3,2,1]
    aaa=s.IsPopOrder(s,aa,aa1)
    print(aaa)