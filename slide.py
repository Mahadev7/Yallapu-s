arr = [1,3,-1,-3,5,3,6,7]
k = 3
n = len(arr)
l = []
for i in range(n-k+1):
    p = max(arr[i:i+k])
    l.append(p)
print(l)
