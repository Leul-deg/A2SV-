class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        tx , ty = king
        #right
        while tx < 8:
            tx += 1
            if [tx,ty] in queens:
                res.append([tx,ty])
                break
            
        #left
        tx , ty  = king
        while tx >=0:
            tx -= 1
            if [tx,ty] in queens:
                res.append([tx,ty])
                break
                
        
        #up
        tx, ty = king
        while ty >= 0:
            ty -= 1
            if [tx, ty] in queens:
                res.append([tx, ty])
                break
        
        #down
        tx, ty = king
        while ty < 8:
            ty += 1
            if [tx, ty] in queens:
                res.append([tx,ty])
                break
        
        #right up
        tx, ty = king
        while tx < 8 and ty >= 0:
            tx += 1
            ty -= 1
            if [tx, ty] in queens:
                res.append([tx,ty])
                break
        
        
        #right down
        tx, ty = king
        while tx < 8 and ty < 8:
            tx += 1
            ty += 1
            if [tx, ty] in queens:
                res.append([tx, ty])
                break
            
        
        #left up
        tx , ty = king
        while tx >= 0 and ty >= 0:
            tx -= 1
            ty -=1
            if [tx, ty] in queens:
                res.append([tx,ty])
                break
        #left down
        tx, ty = king
        while tx >= 0 and ty < 8:
            tx -= 1
            ty += 1
            if [tx,ty] in queens:
                res.append([tx,ty])
                break
        return res