class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hashmap = {}
        for winner, loser in matches:
            win_val = hashmap.get(winner , [0,0])
            win_val[0] += 1
            hashmap[winner] = win_val
            los_val = hashmap.get(loser , [0,0])
            los_val[1] += 1
            hashmap[loser] = los_val
        ans = [[] , []]
        for key in hashmap:
            win , lose = hashmap[key]
            if lose == 0:
                ans[0].append(key)
            elif lose == 1:
                ans[1].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans