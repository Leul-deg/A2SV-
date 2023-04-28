class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [ (1 , 0 ) , (0 , 1) , ( 0   , -1) , ( -1 ,  0 )]
        seen = set()
        ROWS ,  COLS = len(maze) , len(maze[0])
        inbound = lambda a , b : 0 <= a < ROWS and 0 <= b < COLS
        isEdge = lambda a , b : a == 0 or a + 1 == ROWS or b + 1 == COLS or b == 0

        q = deque()
        pop_count = 1
        res = 0
        q.append((entrance[0] , entrance[1]))
        seen.add((entrance[0] , entrance[1]))


        while q : 

            for _ in range(pop_count):

                x , y = q.pop()

                if isEdge(x , y) and res:
                    return res


                for dx , dy in directions:
                    if inbound(x + dx , y + dy) and (x + dx  , y + dy) not in seen and maze[x + dx][y + dy] == '.':
                        q.appendleft((x + dx , y + dy))
                        seen.add((x + dx, y + dy))
                
            pop_count = len(q)
            res += 1

        return -1