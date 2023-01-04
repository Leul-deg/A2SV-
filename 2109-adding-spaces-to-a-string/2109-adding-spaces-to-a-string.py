class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        cur_word = ""
        space_index = 0
        for idx in range(len(s)):
            char = s[idx]
            if space_index < len(spaces) and  idx == spaces[space_index]:
                space_index += 1
                res.append(cur_word)
                cur_word = ""
            cur_word += char
        res.append(cur_word)
        return " ".join(res)
            