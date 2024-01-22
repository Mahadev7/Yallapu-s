nums = [4,3,2,4]
x = 2
l = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        p = (nums[i],nums[j])
        l.append(p)
print(l)
