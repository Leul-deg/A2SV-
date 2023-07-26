class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        _max  , res = -inf , -inf

        for cur in values:

            res = max(res , _max + cur)

            _max -= 1
            cur -= 1

            _max = max(cur , _max)
        
        return res