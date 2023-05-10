class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        ans = [[] for _ in range(n)]

        for end , start  in edges:
            adj[start].append(end)
        
        def dfs(node):

            if node in seen:
                return ans[node] + [node]
            
            res = []
            for neg in adj[node]:
                res += dfs(neg)
            
            seen.add(node)
            res = set(res)
            res = list(res)
            res.sort()
            ans[node] = res
            
            return res + [node]

            


            
        print(adj)
        seen = set()
        for i in range(n):
            dfs(i)
        
        return ans