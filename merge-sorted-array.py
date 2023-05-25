class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        one  , two = m - 1 , n - 1
        write = len(nums1) - 1
        while two > -1:
            # print(one , two , "hey", 'write', write)
            # print(nums1, nums2)
            if one > -1 and  nums1[one] > nums2[two] :
                nums1[write] = nums1[one]
                nums1[one] =0 
                one -= 1
            else:
                # print(one , two , "hey", 'write', write)

                nums1[write]  = nums2[two]
                two -= 1
                # print(one , two , "hey", 'write', write,"in")

            
            write -= 1