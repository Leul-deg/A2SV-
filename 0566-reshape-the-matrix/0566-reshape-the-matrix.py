class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat) * len(mat[0]):
            return mat
        temp = []
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                temp.append(mat[x][y])
        new_mat  = [
            
        ]
        
        idx = 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(temp[idx])
                idx += 1
            new_mat.append(row)
                
                
                
        return new_mat