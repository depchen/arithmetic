
def binary_search(a,low,top,obj):
    if len(a) == 0:
        return -1
    while(low<=top):
        mid=int((low+top)/2)
        if a[mid] == obj:
            return mid
        elif a[mid] < obj:
            low=mid+1
        else:
            top=mid-1
    return -1

def insert_search(a,low,top,obj):
    if len(a) == 0:
        return -1
    while(low<=top):
        mid=low+int((top-low)*((obj-a[low])/(a[top]-a[low])))
        if a[mid] == obj:
            return mid
        elif a[mid] < obj:
            low=mid+1
        else:
            top=mid-1
    return -1


if __name__ == "__main__":
    input_data=[3,3,5,6,7,8,34,245,567,676,2345]
    output1=binary_search(input_data,0,len(input_data)-1,5)
    output2=insert_search(input_data,0,len(input_data)-1,5)
    print(output1+1)
    print(output2 + 1)