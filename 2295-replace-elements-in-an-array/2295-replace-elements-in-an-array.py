class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap = {}
        for idx in range(len(nums)):
            num = nums[idx]
            hashmap[num] = idx
        
        for x , y in operations:
            
            nums[hashmap[x]] = y
            
            idx = hashmap[x]
            hashmap.pop(x)
            hashmap[y] = idx
            
        
        return nums
        