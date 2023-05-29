class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        ways  = 0 
        n  = len(nums)
        memo = {}
        def backtrack(idx , _sum):
            
            if (idx , _sum) in memo:
                return memo[(idx , _sum)]

            nonlocal ways
            a, b = 0 ,  0  
            if idx >= n:
                if _sum ==  target:
                    return 1
                return 0  
                
            a = backtrack(idx + 1 , _sum + nums[idx])
            b = backtrack(idx + 1 , _sum - nums[idx])

            memo[(idx , _sum)] = a + b
            return a + b

        
        return backtrack(0 , 0)

        # return ways