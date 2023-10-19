class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succ: List[float], start: int, end: int) -> float:

        graph =  [[] for _ in range(n)]

        for idx in range(len(edges)):

            u,v = edges[idx]
            graph[u].append((v , -math.log(succ[idx] , 10) ))
            graph[v].append((u  , -math.log(succ[idx] , 10)))
        
        heap = [(0 , start)]
        seen = set()

        while heap :

            prob , node = heappop(heap)

            if node == end :

                return 10 **( -prob)
            
            seen.add(node)

            for neg , weight in graph[node]:

                if neg not in seen :

                    heappush(heap , (prob  + weight , neg ))
        
        return 0