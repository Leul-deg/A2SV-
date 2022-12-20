class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        a,b,c = len(nums) - 3, len(nums) - 2,len(nums)-1
        nums.sort()
        while a >= 0:
            if nums[a] + nums[b] > nums[c] :
                return nums[a] + nums[b] + nums[c]
            a -= 1
            b -= 1
            c -= 1
        return 0
        
        