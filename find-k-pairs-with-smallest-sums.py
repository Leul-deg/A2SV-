class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) :
        n1  , n2 = len(nums1) , len(nums2)
        heap  = []
        for idx in range(n1):
            _sum = nums1[idx] + nums2[0]
            heappush(heap  , (_sum , idx , 0))
        res = []

        while len(res) < k and heap:
            _sum , idx1 , idx2 = heappop(heap)

            res.append([nums1[idx1] , nums2[idx2]])

            idx2 += 1

            if idx2 < n2:

                new_sum = nums1[idx1] + nums2[idx2]

                heappush(heap , (new_sum  , idx1 , idx2))
        
        return res