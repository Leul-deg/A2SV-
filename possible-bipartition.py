class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        adj = [[] for i in range(0, n + 1)]


        for src , dest in dislikes:
            adj[src].append(dest)

        colors = {}

        def dfs(node , color):

            if node in colors and  color == colors[node]:
                return True

            if node in colors and colors[node] != 5 and color != colors[node]:
                return False
            
            colors[node] = color

            res  = True
            for neighbor in adj[node]:
                res = res and dfs(neighbor , -1 * color)
            
            return res 
        
        ans = True
        for i in range(1 , n + 1):
            
            if i not in colors:
                ans = ans and dfs(i , 1)
            
            for c in colors:
                colors[c]  = 5
            
        
        return ans