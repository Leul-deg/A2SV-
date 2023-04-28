class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for p  ,c in edges:
            graph[p].append(c)
            graph[c].append(p)
        
        seen = set()
        def dfs(node):

            time =  0
            seen.add(node)
            for neg in graph[node]:

                if neg not in seen:
                    r = dfs(neg)
                    time +=  r + 2 if r >= 0 else 0
            
            if time == 0 and hasApple[node] == 0:
                return -1
            
            if time == 0 and hasApple[node]:
                return 0
            
            return time
        
        a = dfs(0)

        return a if a >= 0 else 0