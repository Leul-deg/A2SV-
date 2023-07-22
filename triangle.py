class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for r in range(len(triangle) - 1 ,  -1 , -1):

            row = triangle[r]

            for idx in range(len(row) - 1):

                triangle[r-1][idx]  += min(row[idx]  , row[idx + 1])

        
        return triangle[0][0]