import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * weight for weight in stones ]
        heapq.heapify(stones)
        while len(stones)> 1:
            large = -1 * heapq.heappop(stones)
            small  = -1* heapq.heappop(stones)
            if large - small > 0:
                heapq.heappush(stones,-1* (large - small))
            
        if stones:
            return -1*stones[0]
        return 0