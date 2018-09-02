# 题目描述
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        a=[]
        b=[]
        m=0
        n=0
        for i in range(len(array)):
            if array[i] % 2 == 1:
                a.append(array[i])
                m=m+1
            else:
                b.append(array[i])
                n=n+1
        #a=a.append(b)
        return a+b


if __name__ == '__main__':
    s = Solution
    aa=s.reOrderArray(s,[1,2,3,1,2,3,1,2,3])
    print(aa)