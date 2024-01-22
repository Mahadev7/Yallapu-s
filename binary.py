n = 9
x = 5
arr = [ 1, 3, 5, 5, 5, 5, 67, 123, 125 ]
l,m = [],[]
for i in range(n):
    if arr[i] == x:
        l.append(i)
        break
for i in range(n-1,-1,-1):
    if arr[i] == x:
        l.append(i)
        break
print(l,m)
