class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        store = []
        heapq.heapify(store)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(store)<k:
                    heapq.heappush(store,-1*matrix[i][j])
                else:
                    if store[0]<-1*matrix[i][j]:
                        heapq.heappop(store)
                        heapq.heappush(store,-1*matrix[i][j])
  
        return -1*store[0]