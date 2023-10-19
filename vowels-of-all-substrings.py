class Solution:
    def countVowels(self, s):
        vowels="aeiou"
        res=0
        for i in range(len(s)):
            res+=(len(s)-i)*(i+1) if s[i] in vowels else 0
        
        return res