class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = Counter(s)
        c2 = Counter(t)
        for key in c2:
            if key not in c1 or c2[key] > c1[key]:
                return key
        