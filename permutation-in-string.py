class Solution:
    def checkInclusion(self, s1: str, s: str) -> bool:
        s1_count = Counter(s1)
        window = {}
        l = 0 
        res = False
        for r in range(len(s)):
            
            if s[r] not in s1_count:
                l  = r + 1
                window = {}
                continue
            
            window[s[r]] = window.get(s[r], 0 )  + 1
            
            while window[s[r]] > s1_count[s[r]]:
                window[s[l]] -= 1
                l += 1
        
            res = res or window == s1_count
            
        return res