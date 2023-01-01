class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_to_letter , letter_to_word = {} , {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for idx in range(len(words)):
            word,letter = words[idx], pattern[idx]
            if word not in word_to_letter and letter not in letter_to_word :
                word_to_letter[word] = pattern[idx]
                letter_to_word[letter] = word
            if not(word_to_letter.get(word) == letter and letter_to_word.get(letter) == word):
                return False
        return True            
                
            
        