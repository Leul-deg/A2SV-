class Solution:
    def tribonacci(self, n: int, memo = {}) -> int:

        if n in memo : 
            return memo[n]
        
        if n  ==1 or n == 2:
            return 1
        if n == 0:
            return 0 
        
        ans =  self.tribonacci(n - 1)  + self.tribonacci(n - 2) + self.tribonacci(n - 3 )

        memo[n] = ans 

        return ans