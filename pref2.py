class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        count[0]=1
        ans=prefix=0
        for right in range(len(nums)):
            prefix+=nums[right]
            ans+=count[prefix-k]
            count[prefix]+=1
        return ans
