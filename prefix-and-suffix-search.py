class WordFilter:

    def __init__(self, words: List[str]):


        self.d = defaultdict(int)
        for idx, word in enumerate(words):
            for i in range(len(word)):
                for j in range(len(word)):
                    pre = word[ : i + 1]
                    suf = word[j : ]
                    self.d[(pre, suf)] = idx
        # print(self.d)


        

        

    def f(self, pref: str, suff: str) -> int:
        if (pref, suff) in self.d:
            return self.d[(pref, suff)]
        return -1
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)