class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss , one_loss , more_loss = set() , set() , set()
        for winner , loser in matches:
            if winner not in one_loss and winner not in more_loss:
                zero_loss.add(winner)
            if loser not in zero_loss and loser not in one_loss and loser not in more_loss:
                one_loss.add(loser)
            elif loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser)
                more_loss.add(loser)
        ans = [sorted(list(zero_loss)) , sorted(list(one_loss))]
        return ans
        
                