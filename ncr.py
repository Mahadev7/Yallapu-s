def ncr(n,r):
    res = 1
    for i in range(n-r+1,n+1):
        res *= i
    for i in range(1,r+1):
        res //= i
    return res
n,r = map(int,input().split())
print(ncr(n,r))
