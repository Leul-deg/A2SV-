class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        bob,me,alice = 0, len(piles)-2 , len(piles) -1
        mypile = 0
        while me > bob:
            mypile+= piles[me]
            bob+=1
            me-=2
            alice-=2
        return mypile
            
            
        