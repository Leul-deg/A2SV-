class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap  = []
        heappush(heap , (nums[0], 1))
        r  = 1
        
        while r < len(nums):
            
            n ,  l  = heap[0]
            
            cur  = nums[r]
            #print(heap, cur)
            while heap and cur - 1 > heap[0][0]:
                n, l = heappop(heap)
                if l < 3 :
                    return False 
            #print(heap, cur)
            if heap and cur  - 1 == heap[0][0]:
                
                n, l  = heappop(heap)
                heappush(heap,(cur , l + 1))
            else:
                
                heappush(heap , (cur , 1))
            r += 1
        #print(heap)
        while heap:
            n , l = heappop(heap)
            if l < 3:
                return False 
         
        
        return True