class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        seen  = set()
        pop_count  = 1
        moves = 0
        q = deque()
        q.append('0000')
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        while q :
            # print(q)
            # print(cur)
            for  _ in range(pop_count):
                cur = q.pop()
                
                all_pos = []
                for idx in range(4):
                    num = int(cur[idx])
                    n1 , n2 = (num + 1) % 10 , (num - 1) % 10

                    all_pos.append( cur[:idx] + str(n1) + cur[idx+1 : ])
                    all_pos.append(cur[:idx] + str(n2) + cur[idx + 1:])
                
                for pos in all_pos:
                    if pos not in deadends and pos not in seen:
                        q.appendleft(pos)
                        seen.add(pos)
                
                    if pos == target:
                        return moves+1
            
            pop_count = len(q)
            moves += 1
        
        return -1