class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {}
        def farming(target):

            if target in memo:
                return memo[target]   
            if target < 0 :
                return float('inf')

            if target == 0:
                return 0
            
            res = float('inf')
            for coin in coins:
                res = min(farming(target - coin) , res)
                if target - coin < 0:
                    break

            
            memo[target] = res + 1
            return res + 1

        
        g = farming(amount )

        return g if g != float('inf') else  -1