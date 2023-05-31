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
        
        grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        grid[0][0] = 1
        # print(grid)
        def getter( r  , c):
            if r not in range(0 ,  m ) or c not in range(0 ,  n ):
                return  0 
            
            return grid[r][c]

        for i in range(m):
            for j in range(n):
                if i or j :
                    grid[i][j] = getter(i - 1 , j ) + getter(i , j - 1)
        
        


        return grid[m - 1 ][n - 1]