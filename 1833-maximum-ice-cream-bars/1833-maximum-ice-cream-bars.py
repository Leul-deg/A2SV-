class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        idx = 0
        while coins > 0 and idx < len(costs):
            if coins >= costs[idx]:
                count += 1
                coins -= costs[idx]
                idx += 1
            else:
                break
        
        return count