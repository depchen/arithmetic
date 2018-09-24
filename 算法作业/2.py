import time
#普通快排
#输入：[7,7,3,5,1,5,6,8]
#输出：[1,3,5,5,6,7,7,8]
#耗时：1001.1196136474609ms/1000（由于时间不容易测出，实验时需*1000，结果需/1000）
def quick_sort(a,l,r):
    if l<r:#终止条件
        index=partition(a,l,r) #找到划分点
        quick_sort(a,l,index-1) #对左部分进行递归排序
        quick_sort(a,index+1,r) #对右部分进行递归排序

def partition(a,l,r):
    x=a[l]
    i=l
    j=r  #初始化参数
    while True:
        while x<a[j]:  #从右开始，定位到小于x的位置，即j
            j=j-1
        c=a[i] #进行换位
        a[i]=a[j]
        a[j]=c
        while x>=a[i] and  i<r: #从左开始，定位到大于等于x的位置，即i
            i=i+1
        if i>=j:  # 循环结束条件，即排序结束
            break
        c = a[i]  #进行换位
        a[i] = a[j]
        a[j] = c
    return j  #返回划分节点j

#三者取中快排
#输入：[7,10,3,5,1,5,6,8]
#输出：[1,3,5,5,6,7,8,10]
#耗时：1.87345ms/1000（由于时间不容易测出，实验时需*1000，结果需/1000）
def quick_sort1(a,l,r):
    if l<r:#终止条件
        index=partition1(a,l,r) #找到划分点
        quick_sort(a,l,index-1) #对左部分进行递归排序
        quick_sort(a,index+1,r) #对右部分进行递归排序

def partition1(a,l,r):
    dealPivot(a, l, r) #添加三者取中操作，下面操作如普通操作
    x = a[l]
    i = l
    j = r  # 初始化参数
    while True:
        while x < a[j]:  # 从右开始，定位到小于x的位置，即j
            j = j - 1
        c = a[i]  # 进行换位
        a[i] = a[j]
        a[j] = c
        while x >= a[i] and i < r:  # 从左开始，定位到大于等于x的位置，即i
            i = i + 1
        if i >= j:  # 循环结束条件，即排序结束
            break
        c = a[i]  # 进行换位
        a[i] = a[j]
        a[j] = c
    return j  # 返回划分节点j

# 将左、中、右3个数排序并调序
def dealPivot(arr, left, right):
    mid = (left + right) // 2
    if (arr[left] > arr[mid]):
        swap(arr, left, mid)
    if (arr[left] > arr[right]):
        swap(arr, left, right)
    if (arr[right] < arr[mid]):
        swap(arr, right, mid)
    swap(arr, right, mid)
#换位
def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
#主函数
if __name__ == '__main__':
    start1=time.time()
    a=[7,7,3,5,1,5,6,8]*10
    quick_sort(a,0,len(a)-1)  #第一个元素为枢纽的快速排序方法
    end1=time.time()*1000
    print(a)
    print("耗费时间："+str((end1-start1)))
    start2 = time.time()
    a = [7, 10, 3, 5, 1, 5, 6, 8]*10
    quick_sort1(a, 0, len(a) - 1)  # 三者取中的快速排序方法
    end2 = time.time()*1000
    print(a)
    print("耗费时间：" + str((end2 - start2)))