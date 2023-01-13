class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        for idx in range(len(words)):
            
            word = words[idx]
            char_count = [0]*26
            
            for char in word:
                
                char_count[ord(char) - ord('a')] += 1
            
            words[idx] = char_count
            
        res = []
        
        for idx in range(26):
            minimum = float(inf)
            for char_count in words:
                minimum = min(char_count[idx] , minimum)
            if minimum:
                res += (chr(ord('a') + idx) * minimum)
        
        return res
            
        