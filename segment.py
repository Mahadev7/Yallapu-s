
l,r = map(int,input().split())
d = r-l  + 1 
x = [1] * d
for i in range(2,d):
    if x[i] == 1:
        for j in range(i*i,d,i):
            x[j] = 0
#print(x)
#print(len(x))
hp = getprimes(r)
print(hp)
