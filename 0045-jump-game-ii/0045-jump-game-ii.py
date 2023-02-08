class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [float('inf')]
        size = len(nums)  - 1
        
        def brute_force(idx , moves):
            if idx == size:
                res[0] = min(res[0] , moves)
                return
            if idx > size:
                return
            
            
            if nums[idx] + idx >= size:
                brute_force(size, moves + 1)
                return
            
            final = min(nums[idx] + idx + 1 , size + 1)
            next_index = idx  + 1
            
            for i in range(idx + 1 ,final):
                if nums[next_index] + next_index <= nums[i] + i:
                    next_index = i
                
            
            brute_force(next_index, moves+ 1)
                
                
                
            
        brute_force(0 , 0)
        
        return res[0]
            