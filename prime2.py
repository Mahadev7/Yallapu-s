def Pair(a,b,c):
    if a + b == c:
        return True
    return False
def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
n = 10
l = []
li = []
l2 = []
for i in range(1,n+1):
    if  prime(i):
        l.append(i)
print(l)
d1 = {}
for i in l:
    d = n-i
    if d in l:
        li.append([i,d])
print(li)
for i in li:
    if i == sorted(i):
        l2.append(i)
print(l2)
