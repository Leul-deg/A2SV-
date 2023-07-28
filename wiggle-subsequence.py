class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        high , low = [1] * len(nums) , [1]* len(nums)
     
        for j in range(len(nums) - 1   , -1 , -1 ):

            cur_num = nums[j]
            h , l = 1  , 1

            for i in range(j + 1 , len(nums)):

                if nums[i] > cur_num:
                    h = max(h  , low[i] + 1)
                
                elif nums[i] < cur_num:
                    l = max(l , high[i] + 1)
            
            high[j] , low[j] = h , l 
        
        return max(max(high) , max(low))