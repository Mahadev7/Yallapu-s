class Solution:
    def maxPower(self, s: str) -> int:
        a,b = 1,1
        for  i in range(len(s)-1):
            if s[i] == s[i+1]:
                a+=1
                b = max(a,b)
            else:
                a = 1
        return b
