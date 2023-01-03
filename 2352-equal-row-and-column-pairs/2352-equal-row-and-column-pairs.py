class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        new_grid = []
        for row in grid:
            r = []
            for num in row:
                r.append(str(num))
            
            new_grid.append(r)
        
        rows = [row for row in new_grid]
        cols = []
        
        for idx in range(len(grid[0])):
            col = []
            for row in new_grid:
                col.append(row[idx])
            cols.append(col)
        
        count = 0
        
        for row in rows:
            for col in cols:
                if row == col:
                    count += 1
        return count
            
                