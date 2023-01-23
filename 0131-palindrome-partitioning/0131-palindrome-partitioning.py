class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def backtrack(start , store):
            last = store[-1]
            if last != last[-1::-1]:
                return
            if start == n :
                res.append(store)
                return
            
            
            for idx in range(start+1 , n+1):
                backtrack(idx, store+[s[start:idx]])
        
        for idx in range(1,n+1):
            backtrack( idx , [s[:idx]])
        
        return res
        