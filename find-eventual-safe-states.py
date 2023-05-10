class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = defaultdict(int)
        ans = set()
        def dfs(node):


                if color[node] == -1:
                    return node in ans

                if color[node] == 1:
                    return False
                res = True
                color[node] = 1
                for neg in graph[node]:
                    res = dfs(neg) and res 
                
                if res :
                    ans.add(node)
                
                color[node] = -1
                return res
        for idx in range(len(graph)):
            dfs(idx)
        return sorted(list(ans))