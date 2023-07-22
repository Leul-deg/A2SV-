class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp =  [[0 , 0  , 0] for _ in range(n)]

        dp[0][0] =  -prices[0]

        for idx in range(1 ,  n ):

            buy , sell , cooldown = dp[idx  - 1]

            #buy here you consider sell

            n_buy = cooldown - prices[idx]

            #sell here you consider previous buy

            n_sell = prices[idx] + buy

            #cooldown here

            n_cooldown = sell

            buy , sell , cooldown = max(buy , n_buy) , max(sell , n_sell) , max(cooldown , n_cooldown)

            dp[idx] = [buy , sell , cooldown]

        

        return max(dp[n - 1])