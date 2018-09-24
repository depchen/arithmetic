# 题目描述
# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））
# -*- coding:utf-8 -*-
import sys
class Solution:
    def __init__(self):
        self.list=[]
        self.alist=[sys.maxsize]
    def push(self, node):
        # write code here
        self.list.append(node)
        if node<self.top():
            self.alist.append(node)

    def pop(self):
        # write code here
        if self.alist:
            a=self.list.pop(-1)
            if a == self.top():
                self.alist.pop(-1)
            return a
        else:
            return None

    def top(self):
        # write code here
        if self.alist:
            return self.alist[-1]
        else:
            return None

    def min(self):
        # write code here
        return self.top()

if __name__ == '__main__':
    s=Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.push(4)
    s.push(5)
    print(s.min())