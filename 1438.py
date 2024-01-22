def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
def fun(n):
    l = []
    for i in range(1,n+1):
        if n%i == 0 and prime(i):
            l.append(i)
    return l
nums = [2,4,3,7,10,6]
l = []
for i in range(len(nums)):
    p  = fun(nums[i])
    for  i in p:
        l.append(i)
print(len(set(l)))
