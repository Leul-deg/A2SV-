class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            n_str = str(num)
            seen.add(num)
            
            seen.add(int(n_str[-1::-1]))
        
        return len(seen)
        