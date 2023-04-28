class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        ROWS , COLS = len(mat) , len(mat[0])
        inbound = lambda a , b : 0 <= a < ROWS and 0 <= b < COLS

        directions  = [ (-1 , 0 ) , ( 0 , -1) , (1, 0 ) , (0 ,1)]
        q = deque()
        seen = set()
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] ==0 :
                    q.append((r,c))
                    seen.add((r,c))
        
        # print(q)
        pop_count = len(q)
        levels = 0
        while q:
            
            # print(q)
            for _ in range(pop_count):

                x , y = q.pop()

                if mat[x][y]:
                    mat[x][y] = levels
                for dx , dy in directions:
                    if (x + dx , y + dy) not in seen and inbound(x + dx  , y + dy) :
                        q.appendleft((x + dx , y + dy))
                        seen.add((x + dx , y  + dy))
                
            pop_count = len(q)
            levels += 1
        

        
        return mat