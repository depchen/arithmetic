import time
class Node(object):
    def __init__(self, v, left=None, right=None):
        self.value = v
        self.left = left
        self.right = right

# 层次遍历入口函数
def level_tranverse_iterate(node):
    if not node:
        return 0
    depth = Depth(node)
    print ("depth:", depth)
    for i in range(1, depth+1):
        print_node_at_level(node, i)
        print()

# 计算树高
def Depth(node):
    if not node:
        return 0
    return max(Depth(node.left)+1,Depth(node.right)+1)

# 当level=1时才输出结点
def print_node_at_level(node, level):
    if not node or level < 1:
        return 0
    if level == 1:
        print('',end=str(node.value))
        print('', end=' ')
        return 0
    print_node_at_level(node.left, level-1)
    print_node_at_level(node.right, level-1)

def create_node(str1):
    a={}
    #b=[Node]*len(str)
    j=-1
    node=None
    for i in range(len(str1)):
        if str1[i].isdigit() :
            j = j + 1
            a[j]=Node(int(str1[i]))

        if str1[i] == '(':
            j = j + 1
            a[j] = str1[i]

        if str1[i] == ')':
            if a[j-1] == '(':
                a[j-2]=Node(a[j-2].value,a[j])
                j=j-2
            else :
                a[j-3] = Node(a[j-3].value,a[j-1],a[j])
                j=j-3
    return a[0]




if __name__=="__main__":
    #node = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    time1=time.time()
    str1=input()
    node=create_node(str1)
    level_tranverse_iterate(node)
    time2=time.time()
    print(time2-time1)