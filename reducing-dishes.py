class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        res = 0 
        for i in range(len(satisfaction)):
            cur = 0 
            start = 1
            for j in range(i , len(satisfaction)):
                cur += start * satisfaction[j]
                start += 1
            res= max(cur , res)
        
        return res