# -*- coding:utf-8 -*-
# 题目描述
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        for i in range(32):
            if n & 1:
                count = count + 1
            n = n >> 1
        return count



if __name__ == '__main__':
    s=Solution
    a=s.NumberOf1(s,-5)
    print(a)