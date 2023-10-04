class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnd = False
        self.ending = 0
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str):

       
        curr = self.root
        for c in word:
            if not curr.children[ord(c) - ord('a')]:
                curr.children[ord(c) - ord('a')] = TrieNode()
            curr = curr.children[ord(c) - ord('a')]
            curr.ending += 1
            # print(curr.children, curr.ending)
        
        # print(self.root)

        

    def search(self, word: str) -> bool:
        curr = self.root
        ans = 0
        for c in word:
            n = ord(c) - ord('a')
            if not curr.children[n]:
                return False
            
            curr = curr.children[n]
            ans += curr.ending
        return ans
        

   

    
    




class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            ans.append(trie.search(word))
        return ans