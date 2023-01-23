class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix ,min_prefix , max_prefix = 0 , 0 , 0
        res = float("-inf")
        
        for num in nums:
            prefix += num
            res = max(res , prefix - min_prefix)
            res = max(res, total - prefix + num + max_prefix)
            min_prefix , max_prefix = min(prefix,min_prefix) , max(max_prefix,prefix)
        
        return res
            
            
            
            
            
            
            