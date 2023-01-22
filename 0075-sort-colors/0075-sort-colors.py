class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        the_dict = {0:0 , 1:0 , 2:0}
        for num in nums:
            the_dict[num]+=1
        index = 0
        for i in range(3):
            for j in range(the_dict[i]):
                nums[index]= i
                index+=1
        
                
            
            
        
        
        