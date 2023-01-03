class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = 0
        
        for word in words:
            max_len = max(max_len , len(word))
        
        res = []
        for idx in range(max_len):
            cur = ""
            for word in words:
                if idx < len(word):
                    cur += word[idx]
                else:
                    cur += " "
            res.append(cur.rstrip())
        return res
                