#使用动态规划解决爬楼梯问题
#递归方程：p[i]=p[i-1]+p[i-2]
#边界条件：p[1]=1,p[2]=2
#自顶向下方法
p=[0]*82
def dp(i):
    if p[i]:
        return p[i]
    if i==1:
        return 1
    if i==2:
        return 2
    p[i]=dp(i-1)+dp(i-2)
    return p[i]
#自底向上方法
def dp1(i):
    p[1]=1
    p[2]=2
    for n in range(3,i+1):
        p[n]=p[n-1]+p[n-2]
    return p[n]
if __name__ == '__main__':
    pp = dp(81)
    print(pp)
    pp=dp1(81)
    print(pp)