class Solution:
    def numTeams(self, rating: List[int]) -> int:

        greater = []
        less =  []

        for idx in range(len(rating)):
            g = 0
            l = 0 
            for j in range(idx + 1 , len(rating)):

                if rating[idx] <  rating[j]:

                    g += 1
                
                else:
                    l += 1
            
            greater.append(g)
            less.append(l)
        
        n = len(rating)
        ans = 0 
        for i in range(n):
            for j in range(i + 1 , n ):

                if rating[i] < rating[j]:
                    ans += greater[j]
                
                else:
                    ans += less[j]
        
        
                
        
        return ans