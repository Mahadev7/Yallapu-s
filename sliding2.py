arr = [8,2,4,7]
k = int(input())
n = len(arr)
p = sum(arr[:k])
l = []
ma = p
for i in range(n-k):
    p = p - arr[i] + arr[i+k]
    ma = max(p,ma)
print(ma)
