class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs) // 2 

        @cache
        def dp(idx , c):


            if idx == n * 2 :

                return 0 if c == n else inf
            a = inf
            if c < n : 

                a = min(a , dp(idx + 1  , c + 1)+ costs[idx][0]) 
            
            a = min(a ,  dp(idx + 1 , c ) + costs[idx][1] ) 

            return a 
        
        return dp(0 , 0)