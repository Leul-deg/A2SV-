class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        m,n = len(mat) , len(mat[0])
        temp = [[] for i in range(m+n)]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                temp[r+c].append(mat[r][c])
        
        for i in range(len(temp)):
            if temp[i]:
                if i % 2 == 0:
                    res.extend(list(reversed(temp[i])))
                else:
                    res.extend(temp[i])
        return res
        
        
        
        
        
            
        
        
                