class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l , r = 0 , len(nums)-1
        pairs= 0
        while l < r:
            add = nums[l] + nums[r]
            if add == k:
                pairs += 1
                l += 1
                r -= 1
            elif add > k:
                r-= 1
            else:
                l+= 1
        return pairs