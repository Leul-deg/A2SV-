class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        q = deque()
        q.append(0)
        seen = set()
        seen.add(0)

        while q:

            cur = q.pop()

            for key in rooms[cur]:
                if key not in seen:
                    seen.add(key)
                    q.appendleft(key)
            
        
        return len(seen) == len(rooms)