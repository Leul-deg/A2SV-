class Solution:
    def longestCycle(self, edges: List[int]) -> int:
       
        res = -1
        colors = defaultdict(int)        
        def dfs(node):
           
            if edges[node] == -1:
               
                return (-1 , -1)
           
            nonlocal res
           
           
            if colors[node] == 1:
                return(node , 1)
           
            colors[node] = 1
           
            n , depth = dfs(edges[node])
           
            if n == node:
                res = max(res , depth)
           
            return (n , depth + 1)
           
            colors[node] = -1
       
        for i in range(len(edges)):
           
            if colors[i] == 0:
               
                 dfs(i)
       
       
        return res