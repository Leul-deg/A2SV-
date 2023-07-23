class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        dp = [[0 , 0] for _ in range(len(prices))]

        dp[0][0] = -prices[0] 

        n = len(prices)

        for idx in range(1 , n ):

            zero , one = dp[idx - 1]

            #buy here

            cost_buy_here  = one - prices[idx]

            #sell here 

            profit_here =  zero + prices[idx] - fee

            zero =   max(zero  , cost_buy_here)

            one = max(one , profit_here)

            dp[idx] = [zero  , one]
        
        return max(dp[n-1])