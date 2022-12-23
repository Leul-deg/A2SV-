class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        maximum = 0
        for l , w in matches:
            maximum = max(maximum , l)
            maximum = max(maximum , w)
        count = [0 for i in range(maximum+1)]
        seen = set()
        for winner , loser in matches:
            seen.add(loser)
            seen.add(winner)
            count[loser] += 1
        
        ans = [[] , []]
        
        for idx in range(len(count)):
            if idx in seen:
                if count[idx] == 0:
                    ans[0].append(idx)
                elif count[idx] == 1:
                    ans[1].append(idx)
        return ans
                    
        
                