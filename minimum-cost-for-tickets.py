class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:


        ans = inf
        n = len(days)

        @cache
        def dp(idx , _sum):

            nonlocal ans
            nonlocal n
            if idx >= n :

                ans = min(ans  , _sum)
                return

            #taking 1
            cur = days[idx]
            idx += 1

            for i , val in enumerate([1 , 7 , 30]):

                while idx < n and cur + val > days[idx] :
                    idx += 1
                
                dp(idx , _sum + costs[i])
        
        dp(0 , 0 )

        return ans