n = int(input())
x = list(map(int,input().split()))
l = []
k = 2
for i in range(n):
    for j in range(i,n+1):
        l.append(x[i:j])
print(l)
li = [i for i in l if sum(i) == k]
print(len(li))
print(l)
