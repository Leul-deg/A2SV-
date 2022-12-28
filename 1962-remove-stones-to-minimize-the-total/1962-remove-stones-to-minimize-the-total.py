class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-1*pile for pile in piles]
        heapq.heapify(heap)
        total = sum(piles)
        while k and heap:
            top = -1*heappop(heap)
            a= math.floor(top/2)
            top = top - a
            total -= (a)
            if top:
                heappush(heap,-1*top)
            k -= 1
        return total
    
    