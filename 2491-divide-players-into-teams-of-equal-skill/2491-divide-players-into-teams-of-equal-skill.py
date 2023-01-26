class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort() 
        l , r = 0  , len(skill)-1
        cur = skill[l] + skill[r]
        res = 0
        while l < r:
            add = skill[l] + skill[r]
            if add != cur:
                return -1
            res += skill[l] * skill[r]
            l+= 1
            r-=1
        
        return res
            
        