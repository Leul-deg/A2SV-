class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new = [num for num in nums]
        new.sort()
        hashmap = {}
        for index , num in enumerate(new):
            if num not in hashmap:
                hashmap[num] = index
            
        ans  = []
        for num in nums:
            ans.append(hashmap[num])
        return ans
        
        
        
        
        
        
            
        
        