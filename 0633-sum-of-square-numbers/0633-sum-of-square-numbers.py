class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        pos = [num for num in range(0, math.ceil(c**(0.5))+1)]
        l , r = 0 , len(pos)  - 1
        while l <= r:
            res = pos[l]**2 + pos[r]**2
            if res == c:
                return True
            elif res > c:
                r -= 1
            else:
                l += 1
        return False
        
        