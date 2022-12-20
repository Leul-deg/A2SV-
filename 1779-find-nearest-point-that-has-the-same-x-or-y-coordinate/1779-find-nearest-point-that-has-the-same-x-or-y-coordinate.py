class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        distance = float(inf)
        index = 0
        flag = False
        for i,item in enumerate(points):
            a,b = item
            if a == x or b == y:
                flag = True
                cur_distance  = abs(a-x) + abs(b-y)
                if cur_distance < distance:
                    index = i
                    distance = cur_distance
                
        if flag:
            return index
        return -1
        