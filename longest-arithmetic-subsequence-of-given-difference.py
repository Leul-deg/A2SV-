class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        res = 0
        hashmap = {}
        for num in arr:
            find = -1 * difference + num
            cur = hashmap.get(find , 0) + 1

            hashmap[num] = cur

            res = max(res , cur)
        
        return res