# 题目描述
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
# 打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

#直接采用 ’ = ’ 赋值方式会使得两个变量占用同一地址，也就是说a 与 b 是同一个对象。
# 而采用切片方式赋值则不会。但是这种浅拷贝方式在二维数组中，直接赋值到二维变量上则也会改变。
# 但是对二维数组的一维数值赋值则不会发生错误。
#也可以采用a.copy()的方式深拷贝，来避免二维赋值的改变值的错误。

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        max_flag=0
        max_len=0
        numbers_copy=numbers[:]
        for n in numbers_copy:
            if max_len<len(str(n)):
                max_len=len(str(n))
            if max_flag<int(str(n)[0]):
                max_flag=int(str(n)[0])
        for i,n in enumerate(numbers_copy):
            numbers_copy[i]=str(n).ljust(max_len,str(max_flag))
        for i in range(len(numbers_copy)):
            for j in range(i+1,len(numbers_copy)):
                if numbers_copy[i]>numbers_copy[j]:
                    t=numbers_copy[i]
                    numbers_copy[i]=numbers_copy[j]
                    numbers_copy[j]=t
                    tt=numbers[i]
                    numbers[i] = numbers[j]
                    numbers[j] = tt
        return str("".join([str(x) for x in numbers]))

if __name__ == '__main__':
    s=Solution()
    a=[23,23,236]
    print(s.PrintMinNumber(a))