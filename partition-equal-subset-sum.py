class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return False
        total = sum(nums)
        if total & 1:
            return False
        
        total //=2
        dp = [[False] * (total + 1) for _ in range(len(nums))] 
        print(len(dp) , len(dp[0]))
        dp[0][0]  = True 
        if nums[0] < len(dp[0]):
            dp[0][nums[0]] = True 
        ans = dp[0][total]
        for idx in range(1 , len(dp)):

            prev = dp[idx - 1]
            num = nums[idx]
            for i in range(len(dp[0])):

                cur = i
                one = prev[i]

                two = False 

                if cur - num >= 0 :

                    two = prev[cur - num]
                
                dp[idx][i] = one or two
            
            ans = dp[idx][total] or ans 
        
        return ans