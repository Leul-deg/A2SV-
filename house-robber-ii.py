class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(arr):

            # print(arr)

            def getter(index):

                if index < 0 :
                    return 0

                return arr[index] 
            
            
            # print(len(arr))
            for idx in range(len(arr)):
                # if idx == 2 and arr == [2 , 1 ,1]:
                #     print(getter(idx - 2))

                arr[idx] = max(getter(idx - 2) + arr[idx] , getter(idx - 1))
            
            # print(arr , "after")
            return max(arr) if arr else -inf
        
        return max(dp(nums[1:]) , dp(nums[:len(nums) - 1]) , nums[0])