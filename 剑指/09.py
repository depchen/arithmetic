# -*- coding:utf-8 -*-
# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:
    def jumpFloor(self, number):
        # write code here
        #递归法  时间长
        # if number == 1:
        #     return 1
        # if number == 2:
        #     return 2
        # return self.jumpFloor(self,number-1)+self.jumpFloor(self,number-2)
        #规律法
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            a = [1, 2]
            for i in range(2, number):
                s=0
                for j in range(i):
                    s=s+a[j]
                a.append(s+1)
            return a[number - 1]

if __name__ == '__main__':
    s=Solution
    a=s.jumpFloor(s,3)
    print(a)