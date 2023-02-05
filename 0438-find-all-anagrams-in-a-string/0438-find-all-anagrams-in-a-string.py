class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        l,r,c = 0 , 0 , Counter(p)
        res = []
        have,need,window = 0 , len(c) , {}
        #creating the first window
        while r < len(p):
            char = s[r]
            if char not in window:
                window[char] = 0
            window[char] += 1
            if char in c:
                if  window[char] == c[char]:
                    have += 1
                elif window[char] == c[char] + 1:
                    have -= 1
            r += 1
        if have == need:
            res.append(l)
        print(r)
        while r < len(s):
            rem , add = s[l] , s[r]
            if rem == add:
                l += 1
                r += 1
                if have == need:
                    res.append(l)
                continue
            window[rem] -= 1
            if add not in window:
                window[add] = 0
            window[add] += 1
            if rem in c:
                if c[rem] == window[rem]:
                    have += 1
                elif c[rem]  == window[rem]+1:
                    
                    have -= 1
            if add in c:
                
                if c[add] == window[add]:
                    have += 1
                elif c[add] +  1 == window[add]:
                    have -= 1
            if have == need:
                res.append(l+1)
            l += 1
            r += 1
            
        return res