class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap= {0:1}
        prefix= 0
        count = 0
        for num in nums:
            prefix += num
            count += hashmap.get(prefix%k , 0)
            hashmap[prefix%k] = hashmap.get(prefix%k , 0) + 1
        
        return count
            
            