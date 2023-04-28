class Solution:
    def racecar(self, target: int) -> int:

        q = deque()
        q.append((0 , 1))
        seen =  set()
        seen.add((0 , 1))

        pop_count = 1
        levels =  0
        while q :


            for _ in range(pop_count):
                pos  , speed  = q.pop()
                if pos == target:
                    return levels
                
                # use a 

                pos1 , speed1 = pos + speed , speed * 2
                
                speed2  = -1 if speed > 0 else 1

                if (pos1 , speed1 ) not in seen:
                    q.appendleft((pos1 , speed1))
                    seen.add((pos1 , speed1))
                
                if (pos , speed2) not in seen:
                    q.appendleft((pos , speed2))
                    seen.add((pos , speed2))
            
            pop_count = len(q)
            levels += 1