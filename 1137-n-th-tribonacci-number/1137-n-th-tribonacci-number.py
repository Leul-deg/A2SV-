class Solution:
    def tribonacci(self, n: int) -> int:
        hashmap = {0:0 , 1: 1 , 2:1}
        def ans(t):
            if t in hashmap:
                return hashmap[t]
            res = ans(t-3) + ans(t-2) + ans(t-1)
            hashmap[t] = res
            return res
        
        return ans(n)
            