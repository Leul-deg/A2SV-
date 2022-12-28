class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0 , 0
        max_length = 0
        hashmap = {}
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0 )  + 1
            while r - l + 1 - self.max_freq_of_dict(hashmap) > k:
                hashmap[s[l]] -= 1
                l += 1
            max_length = max(max_length , r - l + 1)
        return max_length
            
        
            
    def max_freq_of_dict(self, dictionary):
        max_freq = 0
        for freq in dictionary.values():
            max_freq = max(max_freq, freq)
        return max_freq