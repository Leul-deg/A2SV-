class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []
        prev , post = [] , []
        for num in nums:
            if num < pivot:
                prev.append(num)
            elif num > pivot:
                post.append(num)
        ans = prev + [pivot] * (nums.count(pivot)) + post
        return ans