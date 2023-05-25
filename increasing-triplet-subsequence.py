class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        maximum = nums[0]
        mins = []
        maxs = []
        minimum , maximum = float('inf')  , -float(inf)

        for idx , num in enumerate(nums):
            mins.append(minimum)
            minimum = min(num, minimum)
        for num in reversed(nums):
            maxs.append(maximum)
            maximum = max(maximum , num)
        
        maxs.reverse()
        for idx in range(len(nums)):
            minimum = mins[idx]
            maximum = maxs[idx]
            num = nums[idx]
            if minimum < num < maximum:
                return True
        
        return False