class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}

        @cache
        def dp(num):

            # if num in memo:

            #     return memo[num]

            if num == 0:
                return 1
            if num <0 :
                return 0
            pos = 0 
            for cur in nums:

                pos += dp(num  - cur)
            
            # memo[num] = pos

            return pos
        
        return dp(target)