# -*- coding:utf-8 -*-
# 题目描述
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(s):
        # write code here
        a=s.split(' ')
        return '%20'.join(a)

if __name__ == '__main__':
    s='we are you'
    print(Solution.replaceSpace(s))
