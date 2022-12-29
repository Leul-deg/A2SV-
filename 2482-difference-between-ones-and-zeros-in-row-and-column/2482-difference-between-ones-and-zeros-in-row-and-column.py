class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesr = []
        zerosr = []
        onesc = []
        zerosc = []
        for row in grid:
            c= Counter(row)
            onesr.append(c.get(1 , 0 ))
            zerosr.append(c.get(0 , 0))
        length = len(grid[0])
        for i in range(length):
            zeros , ones = 0 , 0 
            for k in range(len(grid)):
                if grid[k][i] == 0:
                    zeros += 1
                else:
                    ones += 1
            onesc.append(ones)
            zerosc.append(zeros)
        res = []
        for r in range(len(grid)):
            ans = []
            for c in range(length):
                diff = onesc[c] + onesr[r] - zerosc[c] - zerosr[r] 
                ans.append(diff)
            res.append(ans)
        return res
                
                
        
        