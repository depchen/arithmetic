# 题目描述
# 输入n个整数，找出其中最小的K个数。
# 例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,
import sys
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k>len(tinput) or tinput == [] or len(tinput)<=0:
            return None
        a=self.heapsort(self,tinput)
        return a[:k]

    def HeapAdjust(self,input_list, parent, lenth):
        temp=input_list[parent]
        child=parent*2+1
        while child<=lenth:
            if child+1<=lenth and input_list[child]<input_list[child+1]:
                child+=1
            if temp >= input_list[child]:
                break
            input_list[parent]=input_list[child]
            parent=child
            child=child*2+1

        input_list[parent]=temp
        return input_list

    def heapsort(self,input_list):
        lenth = len(input_list)
        # 创建初始堆
        for i in range(int((lenth) / 2))[::-1]:
            input_list = self.HeapAdjust(self,input_list, i, lenth - 1)
        for i in range(1, lenth)[::-1]:
            temp = input_list[0]
            input_list[0] = input_list[i]
            input_list[i] = temp
            # print("第%d趟排序：" % (lenth - i), end='')
            # print(input_list)
            input_list = self.HeapAdjust(self,input_list, 0, i - 1)

        return input_list


if __name__ == '__main__':
    s=Solution
    input_list = [4,5,1,6,2,7,3,8]
    print(s.GetLeastNumbers_Solution(s,input_list,4))