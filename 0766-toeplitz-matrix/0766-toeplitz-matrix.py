class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row , col = len(matrix) , len(matrix[0])
        def down_right(i,j):
            cur= matrix[i][j]
            while i < row and j < col:
                if cur != matrix[i][j]:
                    return False
                i += 1
                j += 1 
            return True
        res = True
        
        for c in range(col):
            res = down_right(0,c) and res
        
        for r in range(row):
            res = down_right(r,0) and res
        
        return res
                
            
        