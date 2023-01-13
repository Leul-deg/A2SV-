class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        to_be_removed = {idx  for idx in range(1,n+1)}
        array = [idx for idx in range(1,n+1)]
        count  = 0
        idx = 0
        
        while len(to_be_removed) > 1:
            
            if array[idx%len(array)] in to_be_removed:
                count += 1
            
            if array[idx % len(array)] in to_be_removed and count == k:
                to_be_removed.remove(array[idx%len(array)])
                count = 0 
            
            idx += 1
        
        for num in to_be_removed:
            return num
            
            
                
            
            