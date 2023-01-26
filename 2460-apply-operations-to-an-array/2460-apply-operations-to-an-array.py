class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for r in range(len(nums)-1):
            if nums[r] == nums[r+1]:
                nums[r] *= 2
                nums[r+1]  =0
        
        non_zeros , zeros = [] , []
        for num in nums:
            if num:
                non_zeros.append(num)
            else:
                zeros.append(num)
        non_zeros.extend(zeros)
        
        return non_zeros