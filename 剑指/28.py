# 题目描述
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        for i in range(len(numbers)):
            #a=numbers[i]
            for j in range(i+1,len(numbers)):
                if numbers[i]<numbers[j]:
                    t=numbers[j]
                    numbers[j]=numbers[i]
                    numbers[i]=t


        if ' '.join(str(i) for i in [numbers[len(numbers)//2]]*(len(numbers)//2+1)) in ' '.join(str(i) for i in numbers):
            return numbers[len(numbers) // 2]
        elif ' '.join(str(i) for i in [numbers[-(len(numbers) // 2)]]*(len(numbers)//2+1)) in ' '.join(str(i) for i in numbers):
            return numbers[-(len(numbers) // 2)]
        else:
            return 0



if __name__ =='__main__':
    s=Solution
    a=[1, 2, 3, 2, 4, 2, 5, 2, 3]
    # a=[1,2,3,2,2,2,5,4,2]
    b=[2,2,2]
    aa=s.MoreThanHalfNum_Solution(s,a)
    print(aa)