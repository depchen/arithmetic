# 题目描述
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        k=[1]*index
        t2=0
        t3=0
        t5=0
        for i in range(1,index):
            k[i]=min(k[t2]*2,k[t3]*3,k[t5]*5)  #能去重，并且能从小到大的顺序
            if k[i]==k[t2]*2:t2+=1
            if k[i] == k[t3] * 3: t3 += 1
            if k[i] == k[t5] * 5: t5 += 1
        return k[index-1]

if __name__ == '__main__':
    s=Solution()
    print(s.GetUglyNumber_Solution(1))