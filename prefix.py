
a = [1,2,3]
k = 3
l = []
res = [sum(a[:i + 1]) for i in range(len(a))]
print(res)
