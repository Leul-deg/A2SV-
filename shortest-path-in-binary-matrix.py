class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        directions = [(1,1) , (1 , -1) , (-1 , 1) , (-1 , -1) , (1 , 0) , (0 , 1) , (-1 , 0) , ( 0 , -1)]
        if grid[0][0] or grid[-1][-1]:
            return -1
        
        seen = set()
        q = deque()
        q.append((0 , 0 ))
        ROWS , COLS = len(grid) , len(grid[0])
        if ROWS == 1 and COLS == 1:
            return 1
        inbound = lambda a , b : 0 <= a < ROWS and 0 <= b < COLS
        pop_count =  1
        levels = 1
        seen.add((0,  0))

        while q :



            for _ in range(pop_count):

                x  , y  =  q.pop()

                # print(x , y)

                for dx , dy in directions :


                    if ( x  + dx  , y + dy) not in seen and inbound(x + dx , y+dy) and grid[x  + dx][y + dy] == 0 : 
                        q.appendleft((x + dx , y + dy))
                        seen.add((x + dx , y + dy))
                    if x + dx == ROWS - 1 and y + dy == COLS - 1:
                        return levels +1
                        # print(levels + 1)
            
            levels += 1
            pop_count = len(q)
        
        return -1