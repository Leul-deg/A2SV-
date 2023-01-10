class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        string = list(boxes)
        
        def from_left(string , index):
            
            count = 0
            for idx in range(0,index):
                if string[idx] == "1":
                    count += index - idx
                    
            return count
        
        def from_right(string , index):
            
            count = 0
            for idx in range( index + 1 , len(string)):
                
                if string[idx] == "1":
                    count += idx - index
            return count
        
        ans = []
        
        for idx in range(len(string)):
            ans.append(from_left(string, idx) + from_right(string, idx))
            
        return ans