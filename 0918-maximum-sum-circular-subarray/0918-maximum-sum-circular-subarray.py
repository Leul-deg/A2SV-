class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        forward = []
        prefix = 0
        for num in nums:
            forward.append(total - prefix)
            prefix += num
        
        till_me_max = []
        prefix = 0
        for num in nums:
            if till_me_max:
                till_me_max.append(max(prefix , till_me_max[-1]))
            else:
                till_me_max.append(0)
            prefix += num
        
        prefix = 0
        min_prefix = 0
        maximum = float("-inf")
        for idx,num in enumerate(nums):
            prefix += num
            maximum= max(maximum , prefix - min_prefix)
            maximum = max(maximum , till_me_max[idx] + forward[idx])
            min_prefix = min(min_prefix , prefix)
        
        return maximum
            
            
            
            
            
            