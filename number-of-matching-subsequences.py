class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        def binary_search(c , index):
            arr = d[c]
            if not arr or arr[-1] < index :
                return -1
            
            if index < arr[0]:
                return arr[0]

            return arr[bisect_left(arr, index) ]

        d = defaultdict(list)
        for idx , char in enumerate(s) : 
            d[char].append(idx)
        
        res = 0 
        for word in words :
            idx = 0 
            for char in word:

                i = binary_search(char , idx)

                if i == -1 :
                    break
                
                idx = i + 1
                
                
            
            else :
                res += 1
                # print(word)
                
        return res