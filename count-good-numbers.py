class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        evens = (n + 1) // 2
        odds = (n ) // 2

        ans = pow(5 , evens, MOD ) * pow(4 , odds , MOD)

        return ans % MOD