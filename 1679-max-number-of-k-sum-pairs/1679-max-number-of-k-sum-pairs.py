class Solution:
    def maxOperations(self, nums: List[int], target: int) -> int:
        c = Counter(nums)
        seen = set()
        output = 0
        for num in c:
            if num not in seen and  (target - num) in c:
                if target - num == num:
                    seen.add(num)
                    output+=c[num]//2
                else:
                    seen.add(num)
                    seen.add(target-num)
                    output+= min(c[num], c[target - num])
        return output
                
        
        