def swap(a,i,j):
    aa=a[i]
    a[i]=a[j]
    a[j]=aa

def partition(a,left,right):
    tail=left-1
    pivot=a[right]
    for i in range(left,right):
        if a[i]<=pivot:
            tail = tail + 1
            swap(a,i,tail)

    swap(a,tail+1,right)
    return tail+1

def quick_sort(a,left,right):
    if left >= right:
        return
    pivot_index=partition(a,left,right)
    quick_sort(a,left,pivot_index-1)
    quick_sort(a,pivot_index+1,right)

if __name__ == "__main__":
    input_array=[1,2,3,2,6,3,5,3,5]
    quick_sort(input_array,0,len(input_array)-1)
    print(input_array)