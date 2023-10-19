class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

    
        graph  = [[] for _ in range(n)]

        for u , v ,  t in times :

            graph[u - 1].append((v -  1  , t))
        
        # print(len(graph))
        heap = [(0 , k-1)]
        seen = set()
        res = -1
        while heap :

            if len(seen) == n :
                return res

            time, cur_node = heappop(heap)

            seen.add(cur_node)

            res = max(time, res)
            # print(cur_node)
            for neg , weight  in graph[cur_node]:
                

                if neg not in seen:

                    heappush(heap , (time + weight , neg ))

            
        
        return res if len(seen) == n else -1