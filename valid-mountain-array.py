class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        l , r = 0  , 1

        while r < len(arr):

            if arr[l] > arr[r]:
                break
            if arr[l] == arr[r]:
                return False
            
            l += 1
            r += 1
        else:
            return False
        
        
        #from l + 1 to the end 

        a = arr[l+1:]
        # print(a)
        # print(reversed(a))
        if list(reversed(a)) == sorted(arr[l+1:]) and a and l and len(set(a)) == len(a) :
            return True
        
        return False