class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def return_max(i , j):
            
            return max(grid[i][j] ,
                       
                      grid[i-1][j-1],
                       
                       grid[i-1][j],
                       
                       grid[i-1][j+1],
                            
                        grid[i][j-1],
                        grid[i][j],
                        grid[i][j+1],
                        grid[i+1][j-1],
                        grid[i+1][j],
                        grid[i+1][j+1]
                            )
        
        
        
        new = []
        for r in range(1, len(grid)-1):
            row = []
            for c in range(1, len(grid[0]) - 1):
                            row.append(return_max(r,c))
            new.append(row)
        return new
            
        