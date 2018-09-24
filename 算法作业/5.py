#实现二路归并排序算法
#输入：[2,5,3,7,5,3,8,10]
#输出：[2,3,3,5,5,7,8,10]
#输入：[1,9,56,3,0,47,2,6]
#输出：[0,1,2,3,6,9,47,56]
#复杂度为：O(nlogn)
def merge(a,b):  #合并
    i=0
    j=0
    c=[]
    #以下操作是将a和b数组合并操作
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i=i+1
        else:
            c.append(b[j])
            j=j+1
    if i==len(a):
        for jj in range(j,len(b)):
            c.append(b[jj])
    else:
        for ii in range(i,len(a)):
            c.append(a[ii])
    return c

def merge_sort(list1):
    if len(list1)<=1:
        return list1
    mid=len(list1)//2
    left=merge_sort(list1[:mid]) #将数组拆分
    right=merge_sort(list1[mid:]) #将数组拆分
    all=merge(left,right) #合并
    return all
#主函数
if __name__ == '__main__':
    a=[2,5,3,7,5,3,8,10]
    c=merge_sort(a)
    print(c)
    a = [1, 9, 56,3, 0, 47, 2, 6]
    c = merge_sort(a)
    print(c)