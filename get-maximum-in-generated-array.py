class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        if n <= 1 : 
            return n 
        nums = [0 , 1 ]
        for idx in range(2 , n+1 ):

            if idx & 1 : 
                a = idx // 2 
                nums.append(nums[a] + nums[a + 1])
            
            else:
                nums.append(nums[idx // 2])
        
        return max(nums)