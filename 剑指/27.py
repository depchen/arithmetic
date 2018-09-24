# 题目描述
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        res =[]
        self.helper(ss,res,'')
        a=set(res)  #去重
        b=list(a)
        c=sorted(b)  #字典排序
        return a

    def helper(self,ss,res,s):
        if not ss:
            res.append(s)
        else:
            for i in range(len(ss)):
                self.helper(ss[:i]+ss[i+1:],res,s+ss[i])




if __name__ == '__main__':
    s=input()
    ss=Solution()
    a=ss.Permutation(s)
    print(a)