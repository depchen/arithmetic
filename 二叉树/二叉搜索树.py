class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None

    # 将二叉树转换为有序双向链表
    def Convert(self, pRootOfTree):
        if pRootOfTree==None:
            return
        self.Convert(pRootOfTree.left)
        if self.listHead==None:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead

    # 获得链表的正向序和反向序
    def printList(self, head):
        while head.right:
            print(head.val, end=" ")
            head = head.right
        print(head.val)
        while head:
            print(head.val, end= " ")
            head = head.left


    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getBSTwithPreTin(self, pre, tin):
        if len(pre)==0 | len(tin)==0:
            return None

        root = TreeNode(pre[0])
        for order,item in enumerate(tin):
            if root .val == item:
                root.left = self.getBSTwithPreTin(pre[1:order+1], tin[:order])
                root.right = self.getBSTwithPreTin(pre[order+1:], tin[order+1:])
                return root

    #查找
    def search(self,treeroot,x):
        if treeroot == None:
            return None
        if treeroot.val==x:
            return True
        elif treeroot.val>x:
            result=self.search(treeroot.left,x)
        else:
            result=self.search(treeroot.right,x)
        return result

    def search1(self,node,treeroot,x):
        if node == None:
            return None,node,treeroot
        if node.val==x:
            return True,node,treeroot
        elif node.val>x:
            return self.search1(node.left,node,x)
        else:
            return self.search1(node.right,node,x)


    #插入
    def insert(self,x,treeroot):
        flag=self.search(treeroot,x)
        if not flag:
            if treeroot.left == None and treeroot.right == None:
                newnode=TreeNode(x)
                if x<treeroot.val:
                    treeroot.left=newnode
                else:
                    treeroot.right=newnode
            if x<treeroot.val:
                self.insert(x,treeroot.left)
            else:
                self.insert(x,treeroot.right)

    #删除
    def delete(self,root,x):
        flag=self.search(root,x)
        if flag:
            flag1,node,parent=self.search1(root,root,x)
            # if node.right==None and node.left==None:  被下面两种情况包含
            #     del node
            if node.left==None:
                if parent.left==node:
                    parent.left=node.right
                else:
                    parent.right=node.right
                del node
            elif node.right==None:
                if parent.left==node:
                    parent.left=node.left
                else:
                    parent.right=node.left
                del node
            else:
                pre=node.right
                if pre.left==None:
                    node.value=pre.value
                    node.right=pre.right
                    del pre
                else:
                    next=pre.left
                    while next.left:
                        pre=next
                        next=next.left
                    node.value=next.value
                    pre.left=next.right
                    del next

    def qianxu(self,root):
        if root is not None:
            print(str(root.val)+" ",end='')
            self.qianxu(root.left)
            self.qianxu(root.right)


    def zhongxu(self,root):
        if root is not None:
            self.zhongxu(root.left)
            print(str(root.val) + " ", end='')
            self.zhongxu(root.right)

    def houxu(self,root):
        if root is not None:
            self.houxu(root.left)
            self.houxu(root.right)
            print(str(root.val) + " ", end='')

class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

if __name__ == '__main__':
    solution = Solution()
    preorder_seq = [4,2,1,3,6,5,7]
    middleorder_seq = [1,2,3,4,5,6,7]
    treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    print(solution.search(treeRoot1, 7))  #查找
    solution.insert(8,treeRoot1)  #插入
    solution.delete(treeRoot1,8)
    print("前序：")
    solution.qianxu(treeRoot1)
    print('')
    print("中序：")
    solution.zhongxu(treeRoot1)
    print('')
    print("后序：")
    solution.houxu(treeRoot1)
    print('')
    head = solution.Convert(treeRoot1)
    solution.printList(head)

            #      4
            #    /   \
            #   2     6
            #  / \   / \
            # 1   3 5   7