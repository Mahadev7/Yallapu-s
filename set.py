n = [7,12,9,8,9,15]
l = []
for i in n:
    c = 0
    while i:
        if i&1:
            c += 1
        i >>= 1
    l.append(c)
print(l)
