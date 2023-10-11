class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()

        def ok(val):

            arr = deque()

            for h in heaters:

                arr.append((h - val , h + val))
            
            for temp in houses:

                while arr and not(arr[0][0] <= temp <= arr[0][-1]):
                    arr.popleft()

            
                if not arr or not(arr[0][0] <= temp <= arr[0][-1]):
                    return False 
            
            return True
        

        l  , r = 0 , max(houses) + max(heaters)  + 1

        res = 0
        while l <= r :

            mid = (l + r) // 2

            if ok(mid):
                res = mid 

                r = mid - 1
            
            else :

                l = mid + 1
        
        return res