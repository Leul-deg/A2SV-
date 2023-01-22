class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        array = list(map(str,nums))
        for i in range(len(array)):
            max_index =  i
            for j in range(i+1,len(array)):
                if self.check(array[j], array[max_index]):
                    max_index = j
            array[i] , array[max_index] = array[max_index] , array[i]
        return str(int("".join(array)))
        
            
    
    
    def check(self, n1,n2):
        if n1+n2 > n2+n1:
            return True
        else:
            return False
        