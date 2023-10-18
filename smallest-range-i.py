class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        _min = min(nums)

        _max = max(nums)

        add = min(_max - _min , k)

        _min += add

        minus = max(_min - _max , -k)

        _max += minus

        return _max - _min