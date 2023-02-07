class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        have, hashmap = 0 ,  {}
        l = 0 
        res = 0
        for r , fruit in enumerate(fruits):
            hashmap[fruit] = hashmap.get(fruit , 0) + 1
            if hashmap[fruit] == 1:
                have += 1
            
            while have > 2:
                hashmap[fruits[l]] -= 1
                if not hashmap[fruits[l]]:
                    have -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
            
        