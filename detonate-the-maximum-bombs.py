class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        distance = lambda a,b,c,d : ((a-c)**2 + (b - d)**2)**0.5
        res  =0 
        def dfs(idx):
            # print(idx, "idx")
            # r = bombs[idx][-1]
            x , y , r  = bombs[idx]
            if idx in seen:
                return 0
            
            res = 0
            seen.add(idx)

            for i in range(len(bombs)):
                j , k, __ = bombs[i]
                a = distance(x , y , j , k)
                # print(a, "distance")


                if i != idx and a <= r:
                    res += dfs(i)
            
            return res + 1
        
        
        for _ in range(len(bombs)):
            seen = set()
            if res != len(bombs):
                res = max(dfs(_) , res)
        
        return res