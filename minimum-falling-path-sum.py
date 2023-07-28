class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        def getter(a , b):
            if a not in range(Rows) or b not in range(Cols):
                return inf 
            return matrix[a][b]
        
        Rows , Cols = len(matrix), len(matrix[0])
        di = [(1,0), (1,1) , (1,-1) ]
        
        for r in range(Rows -2 , -1 , -1):
            cur = inf
            
            for c in range(Cols):
                cur = inf
                for dx , dy in di:
                    cur = min(cur, getter(dx + r , dy + c)) 
                              
                              
                matrix[r][c]   += cur


        return min(matrix[0])