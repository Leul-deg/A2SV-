class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        inbound  = lambda a, b : 1 <= a <= m  and 1 <= b <= n 
        memo = {}
        def dp(r , c):
            # print(r , c )
            if r == m and c == n:
                return  1
            if (r  ,c ) in memo:
                return memo[(r ,c )]
            res = 0 
            if inbound(r + 1 , c ):
                res += dp(r + 1 , c)
            
            if inbound(r , c + 1):
                res += dp(r , c + 1)
            
            memo[(r , c )] = res

            return res 
        return dp(1 , 1)