class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        
        for idx in range(len(strs[0])):
            
            for r in range(1 , len(strs)):
                
                
                if strs[r][idx] < strs[r-1][idx] :
                    count += 1
                    break
            
        return count
                