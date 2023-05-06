class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        c = Counter(s)
        for key in c:
            if c[key] != n/ 4:
                break
        else:
            return 0
        l = 0 
        
        
        def window_is_valid(hashmap):
            
            greater =[ ]
            match = 0
            for key in c:
                if c[key] > n/4:
                    greater.append(key)
            
            for key in greater:
                # print(greater)
                if key in window:
                    if c[key] - window[key] <= n/4:
                        match += 1

            return match == len(greater)
                    
                
                
            
            
        window = {}
        
        res = len(s)
        for r in range(len(s)):
            
            window[s[r]] = window.get(s[r], 0 ) + 1
            
            while window_is_valid(window):
                res = min(r-l + 1 , res)
                window[s[l]] -= 1
                l += 1
        
        return res