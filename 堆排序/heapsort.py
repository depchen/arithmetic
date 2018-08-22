def HeapAdjust(input_list,parent,lenth):
    temp=input_list[parent]
    child=parent*2+1
    while child<=lenth:
        if child+1<=lenth and input_list[child]<input_list[child+1]:
            child+=1
        if temp>input_list[child]:
            break
        input_list[parent]=input_list[child]
        parent=child
        child=parent*2+1
    input_list[parent]=temp
    return input_list

def heapsort(input_list):
    lenth=len(input_list)
    #创建初始堆
    for i in range(int((lenth-2)/2)+1)[::-1]:
        input_list=HeapAdjust(input_list,i,lenth-1)
    for i in range(1,lenth)[::-1]:
        temp=input_list[0]
        input_list[0]=input_list[i]
        input_list[i]=temp
        print("第%d趟排序：" % (lenth-i),end='')
        print(input_list)
        input_list=HeapAdjust(input_list,0,i-1)

    return input_list


if __name__=='__main__':
    input_list=[6,2,1,6,4,2,3,8,7,5,9,1,0,9]
    print("排序前：",input_list)
    output_list=heapsort(input_list)
    print("排序后：",output_list)