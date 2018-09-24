#采用二分查找方法，查找元素值为x的位置
#输入：a=[1,3,5,6,8,9,11,34]  x=12
#输出：小于x的最大元素位置i:6,大于x的最小元素位置j:7
#输入：a=[1,3,5,6,8,9,11,34]  x=34
#输出：等于x的元素位置i:7

def binary_serch(a,l,r,x):
    mid = (l + r) // 2
    while l<=r:
        if a[mid]<x:
            l=mid+1
        elif a[mid]>x:
            r=mid-1
        else:
            return mid   #如果找到x，则返回mid，即为x的位置
        mid = (l + r) // 2
    return l,r  #如果没有找到x，则返回l和r，即为小于x的最大元素位置i 和大于x的最小元素位置 j
#主函数
if __name__ == '__main__':
    a=[1,3,5,6,8,9,11,34]
    print("小于x的最大元素位置i:"+str(binary_serch(a,0,len(a)-1,12)[1])+","
          "大于x的最小元素位置j:"+str(binary_serch(a,0,len(a)-1,12)[0]))
    print("等于x的元素位置i:"+str(binary_serch(a, 0, len(a) - 1, 34)))