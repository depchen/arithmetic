def divid(n,m):
    if n == 1 or m == 1:
        return 1
    elif n<m:
        return divid(n,n)
    elif n>m:
        return divid(n-m,m)+divid(n,m-1)
    else:
        return 1+divid(n,m-1)



if __name__ == '__main__':
    a=divid(6,6)
    print(a)