class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        t = {}
        for idx in range(len(tasks)):
            e , d  = tasks[idx]
            t[idx] = (e , d)
            tasks[idx].append(idx)
        
        tasks.sort()
        heap = []
        heappush(heap, tasks[0][1:])
        r  = 1
        res  = []
        #print(tasks)
        #print(heap)
        tim = tasks[0][0]
        while heap:
            d , i  = heappop(heap)
            e = t[i][0]
            p = r 
            res.append(i)
           # print(t[i], 'hdsj')
            while r < len(tasks) and tasks[r][0] <= tim + d:
                heappush(heap, tuple(tasks[r][1:]))
                
                r += 1
            tim += d
            if not heap and r < len(tasks):
                heappush(heap,tuple(tasks[r][1:]))
                tim = tasks[r][0]
                r += 1
        
        return res