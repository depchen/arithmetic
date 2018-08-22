def dijkstra(a,disk,n,v):
    v[0]=1
    for i in range(1,n-1):
        disk[i-1]=a[0][i]
    u=0
    path=['']*5
    for i in range(1,n):#记录路径，所有能从1到达的点  初始路径都是1，a。如果后面会更新
        if a[0][i]!=-1:
            path[i-1]=str(1)+','+str(i+1)
    for j in range(n-1):
        min=9999
        for i in range(n-1):
            if disk[i]!=-1 and disk[i]<min and v[i+1]==0:
                min=disk[i]
                u=i+1
        v[u]=1
        for i in range(1,n):
            if v[i]==0 and a[u][i]!=-1:
                if disk[i-1]>disk[u-1]+a[u][i] or disk[i-1]==-1:
                    disk[i-1]=disk[u-1]+a[u][i]
                    path[i-1]=str(path[u-1])+","+str(i+1)
    print(disk)
    print(path)
if __name__ == '__main__':
    a=[[-1,2,12,-1,3,-1],
       [-1,-1,3,6,-1,-1],
       [-1,-1,-1,-1,5,-1],
       [-1,-1,4,-1,-1,15],
       [-1,-1,-1,2,-1,4],
       [-1,-1,-1,-1,-1,-1]]
    disk=[-1]*5
    n=6
    v=[0]*6
    dijkstra(a,disk,n,v)