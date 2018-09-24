def sovle(S,T):
    aa=1
    a=[aa]*len(T)
    count=0
    if S == None or T == None or len(S)<len(T):
        return count
    for i in range(1,len(T)):
        for j in range(i):
            if T[j] == T[i]:
               a[i] =a[j]
               break
        if i-1 == j:
            aa=aa+1
            a[i]=aa
    for ii in range(len(S)-len(T)+1):
        bb=1
        b=[bb]*len(T)
        ss=S[ii:len(T)+ii]
        for i in range(1, len(ss)):
            for j in range(i):
                if ss[j] == ss[i]:
                    b[i] = b[j]
                    break
            if i - 1 == j:
                bb = bb + 1
                b[i] = bb
        if a==b:
            count=count+1

    print(count)




if __name__ == '__main__':
    a=input()
    b=input()
    sovle(a,b)