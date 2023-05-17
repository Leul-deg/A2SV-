class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
       
        ind , rows = defaultdict(int) , defaultdict(set)
       
        for u , v in rowConditions:
           
            if v not in rows[u]:
                rows[u].add(v)
                ind[v] += 1
       
        indc , cols = defaultdict(int) , defaultdict(set)
       
        for u , v in colConditions:
           
            if v not in cols[u]:
                cols[u].add(v)
                indc[v] += 1
       
        def top(graph , indegree):
           
            q= deque()
            for key in range(1, k + 1):
                if indegree[key] == 0:
                    q.append(key)
           
            res = []
            while q :
               
                cur = q.pop()
                res.append(cur)
               
                for neg in graph[cur]:
                   
                    indegree[neg] -= 1
                   
                    if indegree[neg] == 0:
                       
                        q.appendleft(neg)
           
            return res
       
        row_order = top(rows , ind)
        col_order = top(cols , indc)
       
        r_index = {num : idx for idx , num in enumerate(row_order)}
        c_index = {num : idx for idx , num in enumerate(col_order)}
       
        matrix = [[0]*k for _ in range(k)]
       
        for num in range(1  , k+ 1):
            if num not in r_index or num not in c_index:
                return []
            matrix[r_index[num]][c_index[num]] = num
       
        return matrix