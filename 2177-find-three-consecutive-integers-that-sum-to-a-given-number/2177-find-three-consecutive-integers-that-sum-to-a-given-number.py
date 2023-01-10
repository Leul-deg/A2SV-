class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        first = int((num - 3)/3)
        
        if 3 * first + 3 == num:
            return [first , first + 1 , first + 2]
        