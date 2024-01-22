import math
def fun(arr):
    s = 0
    p = list(map(int,arr))
    r = p[0]
    if len(p) == 1:
        s += p[0]
    else:
        r = p[0]
        for i in range(1,len(p)):
            r ^= p[i]
    return r
def powerset(arr,n):
    p = (int)(math.pow(2,n))
    l = []
    for i in range(0,p):
        for j in range(0,n):
            if i & (1<<j):
                p = list(map(str,arr))
                c = fun(list(p[j]))
                print(c,end = ' ')
        print('')
            
n = int(input())
x = list(map(int,input().split()))
c = powerset(x,n)
print(c)
