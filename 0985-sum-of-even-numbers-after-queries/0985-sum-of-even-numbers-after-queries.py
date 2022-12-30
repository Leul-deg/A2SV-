class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        total = 0
        res =[]
        
        for num in nums:

            if not num % 2:
                total += num
        
        for val , idx in queries:
            
            if nums[idx] % 2 == 0 and (val + nums[idx]) % 2:
                total -= nums[idx]
            elif nums[idx] % 2 == 0 and not (val+nums[idx]) % 2:
                total += val
            elif nums[idx] % 2 and not (val + nums[idx]) % 2 :
                total += nums[idx]
                total += val
            nums[idx] = nums[idx] + val
            res.append(total)
        
        return res
                