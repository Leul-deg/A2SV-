class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = list(accumulate(nums) )
        res = []
        for q in queries:
            res.append(bisect.bisect_right(prefix, q))
        return res