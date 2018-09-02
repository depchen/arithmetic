# -*- coding:utf-8 -*-
# 题目描述
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39
class Solution:
    def Fibonacci(n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a=[0,1]
            for i in range(2,n+1):
                b=a[i-2]+a[i-1]
                a.append(b)
        return a[n]

if __name__ == '__main__':
    a=6
    b=Solution.Fibonacci(a)
    print(b)