class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows , cols = len(grid) , len(grid[0])
        def dfs(r,c):
            if (r,c) in seen or r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                
                return
            
            seen.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        res = 0
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in seen and grid[i][j] == "1":
                    res += 1
                    dfs(i,j)
        return res
            
        