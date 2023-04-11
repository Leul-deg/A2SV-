class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m  , n = len(grid1) , len(grid2[0])

        inbound = lambda x , y: 0 <= x < m and 0 <= y < n

        directions = [(1,0) , (0,1) , (-1, 0 ) , (0 , -1)]

        def dfs(row , col):
            # print(row , col , "called")
            if grid2[row][col] == 0 :
                return True
            
            res  = True
            if grid1[row][col] == 0:
                res =  False
            
            grid2[row][col] = 0

            for dx , dy in directions:
                if inbound(row + dx , col + dy):
                    res = dfs(row + dx , col + dy) and res
            
            return res
        

        ans = 0
        for i in range(m):
            for j in range(n):
               
                if grid2[i][j] and dfs(i , j):
                    # print(i , j, "add")
                    ans += 1
        
        
        return ans