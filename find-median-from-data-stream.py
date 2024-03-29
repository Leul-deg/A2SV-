class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)
        
        

    def addNum(self, num: int) -> None:
        if self.right:
            if self.right[0]<num:
                heapq.heappush(self.right,num)
            else:
                heapq.heappush(self.left,-1*num)
        else:
            heapq.heappush(self.right,num)
        
        if len(self.right) - len(self.left)>=2:
            removed  = heapq.heappop(self.right)
            heapq.heappush(self.left,-1*removed)
        elif len(self.left) - len(self.right)>=2:
            removed = -1*heapq.heappop(self.left)
            heapq.heappush(self.right,removed)
            
        

    def findMedian(self) -> float:
        if (len(self.left)+ len(self.right)) % 2==0 :
            return (-1*self.left[0] + self.right[0])/2
        if len(self.right)> len(self.left):
            return self.right[0]
        return -1*self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()