class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):
            k = k % len(nums)
            
        output = []
        stack = []
        r = len(nums)-1
        for index in range(k):
            stack.append(nums[r-index])
            nums[r-index] = None
        l = len(nums) - k-1
        while l > -1:
            nums[l] , nums[r]  = nums[r] , nums[l]
            l-=1
            r-=1
        for i in range(k):
            nums[i] = stack.pop()