class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        count = 0
        temp = nums[0]
        some = 0
        nums[0] = nums[some]
        while some < len(nums):
            if temp!= nums[some]:
                count+=1
               
                nums[count] = nums[some]
                
                temp = nums[count]
            some+=1
        return count+1
            
            
            
     
            
            
            
            
        