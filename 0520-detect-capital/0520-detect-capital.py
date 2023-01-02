class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital, small = 0 , 0 
        for char in word:
            asci = ord(char)
            if 64 < asci < 91:
                if small:
                    return False
                capital += 1
            else:
                small += 1
        if capital == len(word) or small == len(word) or capital == 1:
            return True
        