class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        def backtrack(start,store, length):
            last = store[-1]
            if int(last) > 255 or (len(last) > 1 and last[0] == "0" ) or len(store)> 4:
                return
            if len(store) == 4 and length == n:
                res.append(".".join(store))
                return
            
            
            
            for idx in range(start + 1 , n+1):
                backtrack( idx, store + [s[start:idx]], length + idx - start)
        
        for idx in range(1,4):
            backtrack(idx, [s[:idx]], idx)
            
        
        return res
                
        