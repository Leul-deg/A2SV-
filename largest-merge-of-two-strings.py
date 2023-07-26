class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:


        def choose(idx1 , idx2):


            while idx1 < len(word1) and idx2 < len(word2):

                if word1[idx1] == word2[idx2]:

                    idx1 +=  1
                    idx2 += 1
                
                else :
                    if word1[idx1] > word2[idx2]:
                        return True
                    
                    else:
                        return False
            
            return True if idx1 < len(word1) else False
                
        res = []
        one , two = 0 , 0 
        word1 = list(word1)
        word2 = list(word2)
        while one < len(word1) and two < len(word2):

            if word1[one] > word2[two]:

                res.append(word1[one])
                one += 1
            
            elif word2[two] > word1[one]:

                res.append(word2[two])
                two += 1
            
            else:

                if choose(one + 1 , two + 1):

                    res.append(word1[one])

                    one += 1
                
                else:
                    
                    res.append(word2[two])

                    two += 1
        

        res.extend(word1[one:])
        res.extend(word2[two:])

        return "".join(res)