class KthLargest(object):

    
    def __init__(self, k, nums):
        self.k = k
        self.pool = nums
        heapq.heapify(self.pool)
        while len(self.pool)>k:
            heapq.heappop(self.pool)
        

            
    def add(self, val):
        heapq.heappush(self.pool , val)
        if len(self.pool)>self.k:
            heapq.heappop(self.pool )
            
        return self.pool[0]