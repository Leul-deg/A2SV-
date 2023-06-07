class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        first , second = cost[-1] , cost[-2]

        for idx in range(len(cost) - 3 , -1 , -1 ):
            cur = min(first , second) + cost[idx]
            first , second  = second , first 

            second = cur
        
        return min(first , second)