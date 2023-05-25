class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) <= 3:
            return 0 
        
        res = float('inf')
        #first three
        last = nums[-1]
        first = nums[3]
        res = min(res , abs(first - last))
        #last three
        first = nums[0]
        last = nums[-4]
        res = min(res  , abs(first - last))
        #one from first
        first = nums[1]
        last = nums[-3]
        res = min(res , abs(first - last))
        #two from first
        first = nums[2]
        last = nums[-2]
        res = min(res , abs(first - last))

        return res