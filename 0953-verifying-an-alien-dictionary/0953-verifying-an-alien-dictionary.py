class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap  = {}
        for index, char in enumerate(order):
            hashmap[char] = index
        def compare(word1 , word2):
            length = min(len(word1) , len(word2))
            for i in range(length):
                if hashmap[word1[i]] > hashmap[word2[i]]:
                    print(i, "from inside")
                    return False
                elif hashmap[word1[i]] != hashmap[word2[i]]:
                    return True
            if len(word1) > len(word2):
                return False
            return True
        a, b = 0 , 1
        while b < len(words):
            if not compare(words[a] , words[b]):
                print(a,b)
                return False
            a += 1
            b += 1
        return True
            