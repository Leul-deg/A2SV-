class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        stack  = []
        ans = list(range(len(arr)))
        for idx , num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                ans[stack.pop()] = idx
            
            stack.append(idx)
        # print(ans)
        for idx in range(len(arr) - 1 , -1 , -1):

            if ans[idx] != idx:
                # arr[idx] , arr[ans[idx]]   = arr[ans[idx]] , arr[idx]
                start = idx
        
                break
        else:
            # print("shoot")
            return arr
        
        a = list(range(start + 1, len(arr)))
        # print(a, "gee")
        a.sort(key = lambda x : arr[x] , reverse = True)
        # print(a, "a")
        for idx in a:
            if arr[start] > arr[idx]:
                arr[start] , arr[idx] = arr[idx] , arr[start]
                return arr


[1,9,4,6,7]
[1,7,4,6,9]