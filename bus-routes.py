class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        seen = set()
        q , ends = deque()  ,  set()
        d = defaultdict(list)
        for idx  , route in enumerate(routes):
            for stop in route:
                d[stop].append(idx)
                if stop == source:
                    q.append(idx)
                    seen.add(idx)
                
                if stop == target:
                    ends.add(idx)
        
        pop_count = len(q)
        buses = 1

        while q:

            for _ in range(pop_count):
                
                cur = q.pop()
                bus_stops = routes[cur]
                if cur in ends:
                    return buses

                for bus_stop in bus_stops:
                    for neg in d[bus_stop]:
                        if neg not in seen:
                            q.appendleft(neg)
                            seen.add(neg)
            pop_count = len(q)
            buses += 1
        
        return -1