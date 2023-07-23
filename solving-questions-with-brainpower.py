class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        maxs = [0 for idx in range(len(questions) + 1)]



        for idx in range(len(questions) - 1 , -1 , -1):

            points , off = questions[idx]

            cur = points

            if off + 1 + idx < len(questions):

                cur += maxs[idx + 1 + off]
            
            maxs[idx] = max(maxs[idx + 1] , cur)

        
        return max(maxs)