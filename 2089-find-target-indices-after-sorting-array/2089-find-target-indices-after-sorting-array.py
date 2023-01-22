class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [index for index , item in enumerate(nums) if item == target]
    
        
        
            