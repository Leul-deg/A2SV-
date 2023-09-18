class Solution:
    def calculateMinimumHP(self, d: List[List[int]]) -> int:
        
        d[-1][-1] = min(d[-1][-1], 0)
        for r in range(len(d)- 1 , - 1 , -1):
            for c in range(len(d[0])-1 , -1 , -1):

                if r == len(d) - 1 and c == len(d[0]) - 1:
                    continue
                
                elif r == len(d) - 1 :
                    d[r][c] = min(d[r][c + 1] + d[r][c], 0)
                elif c == len(d[0]) - 1:
                    d[r][c] = min(d[r + 1][c] + d[r][c], 0)
                else:
                    d[r][c] = max(min(d[r + 1][c] + d[r][c], 0), min(d[r][c + 1] + d[r][c], 0))
        print(d)
        return max(1 - d[0][0], 1)