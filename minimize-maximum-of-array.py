class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def binary_search(target):
            if nums[0] > target:
                return False
            new = nums.copy()
            for idx , num in enumerate(new):
                if idx:
                    
                    # new[idx - 1] += num - target
                    take = target  - new[idx - 1]
                    new[idx - 1] += take
                    new[idx] = num  - take

                
                if new[idx] > target:
                    return False
            
            return True
        
        l , r = nums[0] , max(nums)

        res = r

        while l <= r:
            mid = (l + r) // 2
            if binary_search(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        print(binary_search(5))
        return res