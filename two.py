n = 9
x = 5
arr = [ 1, 3, 5, 5, 5, 5, 67, 123, 125 ]
i = 0
j = n-1
l,m = -1,-1
while i<=j:
    if arr[i] == x :
        l = i
    elif arr[j] == x:
        m = j
    elif arr[i] < x:
        i += 1

    else:
        j -=1
        
print(l,m)
