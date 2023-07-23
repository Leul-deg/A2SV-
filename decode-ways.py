class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        memo = {}
        def dp(idx):


            if idx in memo:
                return memo[idx]


            if idx == n :
                return 1
            
            # if idx >  n :
            #     return 0 

            if s[idx] == '0':

                return 0
            
            
            #take the first

            res = 0 

            res  += dp(idx  + 1)

            if idx + 2 <= n and int(s[idx]  + s[idx + 1]) <= 26 :

                res += dp(idx + 2)
            
            memo[idx] = res

            return res
        
        return dp(0)