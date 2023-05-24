class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        new_matrix = []
        for c in range(n):
            row = []
            for r in range(n-1 , -1 , -1):
                row.append(matrix[r][c])
            new_matrix.append(row)
        
        for r in range(n):
            for c in range(n):
                matrix[r][c] = new_matrix[r][c]