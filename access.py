n,m = 6,3
x = [5,7,12,11,13,10]
y = [1,2,4]
p = max(y)
c = n - p
a1 = x[:c]
b1 = x[c:]
print(*(a1 + sorted(b1)))
