# 题目描述
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        s = 1.0
        for _ in range(abs(exponent)):
            s = s * base
        if exponent > 0:
            return s
        else:
            return 1 / s

if __name__ == '__main__':
    s = Solution
    print(s.Power(s,2,-3))