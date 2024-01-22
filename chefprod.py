def sums(arr,n):
    s = 0
    for i in arr:
        s += i
    if s == n:
        return True
    return False
def prod(arr):
    p = 1
    for i in p:
        p *= i
    if p&1:
        return True
    return False
n = int(input())
x = [ i for i in range(1,n)]
l = []
for i in range(n):
    for j in range(i+1,n+1):
        l.append(x[i:j])
li = []
for i in l:
    if sums(i,n) and prod(i):
        li.append(len(i))
print(li)
print(l) 
