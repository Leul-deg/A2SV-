class Solution:
    def minDistance(self, s1: str, s2: str) -> int:

        n1 , n2 = len(s1) , len(s2)
        @cache
        def dfs(idx1 , idx2):

            if idx1 == n1 or idx2 == n2:

                return max(n1 - idx1, n2 - idx2)
            
            one = dfs(idx1  + 1 , idx2 + 1) if s1[idx1] == s2[idx2] else  dfs(idx1 + 1 , idx2 + 1) + 1

            two = dfs(idx1 + 1 , idx2) + 1

            three = dfs(idx1 , idx2 + 1) + 1


            return min(one , two , three)

        
        return dfs(0 , 0 )