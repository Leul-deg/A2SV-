class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0 
        start  = len(nums)//2
        res  = []
        for r in range(start , len(nums)):
            res.append(nums[l])
            res.append(nums[r])
            l += 1
        
        return res
        
            
        