class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        n = len(parent)
        print(len(parent) == len(s))
        

        adj = [[] for _ in range(n)]

        for idx, p in enumerate(parent):
            if idx != 0 :
                adj[p].append(idx)
        print(adj)

        visited = set()
        ans = [0]

        def dfs(node):
            heap = []
            # heapify(heap)
            heappush(heap , 0 )
            heappush(heap , 0 )
            visited.add(node)
            for neighbor in adj[node]:
                if s[node] != s[neighbor]:
                    heappush(heap,dfs(neighbor))
                
                if len(heap)  > 2:
                    heappop(heap)
            
            left , right = heappop(heap) , heappop(heap)

            ans[0] = max(ans[0] , left + right + 1)

            return max(left , right) + 1
                







        for idx in range(n):
            if idx not in visited:
                dfs(idx)
        
        return ans[0]