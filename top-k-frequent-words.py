class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        count = [[] for i in range(len(words))]
        for word in c:
            heapq.heapify(count[c[word]])
            heapq.heappush(count[c[word]-1], word)
        output  = []
        for i in range(len(count)-1, -1 ,-1):
            while len(output)<k and count[i]:
                output.append(heapq.heappop(count[i]))
            if len(output)==k:
                return output