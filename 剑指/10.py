# -*- coding:utf-8 -*-
# 题目描述
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            a=[1,2]
            for i in range(2,number):
                a.append(a[i-2]+a[i-1])
            return a[number-1]

if __name__ == '__main__':
    s=Solution
    a=s.rectCover(s,4)
    print(a)