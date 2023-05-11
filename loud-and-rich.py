class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        adj = [[] for _ in range(len(quiet))]
        for start , end  in richer:
            adj[end].append(start)
        
        seen = set()
        ans = [idx for idx in range(len(quiet))]
        def dfs(node):
            if node in seen:
                print("here")
                return ans[node]
            
            res = node
            for neg in adj[node]:
                res = min(dfs(neg) , res , key = lambda x : quiet[x])

            


            seen.add(node)
            ans[node] = res
            return min(node , res , key = lambda x : quiet[x] )
        
        for idx in range(len(quiet)):
            ans[idx] = dfs(idx)
        return ans