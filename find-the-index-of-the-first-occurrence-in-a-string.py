class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        res = 0 
        for r in range(len(haystack)):

            p = 0 

            while p < len(needle) and r < len(haystack) and haystack[r] == needle[p]:

                # print(p , r , "hello")

                p += 1
                r += 1
            
            if p == len(needle):
                return r - p
        
        return -1