class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mysum = sum(nums)
        n = len(nums)
        listsum = n/2 *(n+1)
        return int(listsum - mysum)
        
        