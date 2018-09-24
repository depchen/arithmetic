def test1(a):
    a=list(a)
    tag = [0] * len(a)
    index1 = []
    index2 = []
    for i in range(len(a)):
        if a[i] != '.':
            index1.append(a[i])
            index2.append(i)
    for i in range(len(index1)):
        if index1[i] == 'R' and not tag[index2[i]]:
            for j in range(i+1 , len(index1) ):
                if index1[j] == 'L' and (j+1>=len(index1) or index1[j + 1] == 'R') :
                    m = index2[j]
                    n = index2[i]
                    while n < m:
                        tag[n] = 1
                        tag[m] = 1
                        print(a[n])
                        a[n]='R'
                        a[m]= 'L'
                        n = n + 1
                        m = m - 1
                    break
    for i in range(len(index1)):
        if index1[i]=='R':
            for j in reversed(range(index2[i])):
                if a[j]=='L':
                    for m in range(j+1):
                        a[m]='L'
                        tag[m]=1
            break
    for i in reversed(range(len(index1))):
        if index1[i]=='L':
            for j in range(index2[i],len(a)):
                if a[j]=='R':
                    for m in range(j+1,len(a)):
                        a[m]='R'
                        tag[m]=1
            break

    a = ''.join(a)
    return a



if __name__ == "__main__":
    a = input()
    print(test1(a))
