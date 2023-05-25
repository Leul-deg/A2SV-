class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()
        num = 0
        for idx , number in enumerate(arr):
            if number > num:
                num += 1

        return num