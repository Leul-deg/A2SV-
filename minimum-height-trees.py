class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        indegree = [ 0 for _ in range(n)]
        adj = [[] for _ in range(n)]
        seen = set()
        for start , end in edges:
            indegree[start] += 1
            indegree[end] += 1
            adj[start].append(end)
            adj[end].append(start)
        
        q = deque()

        for idx in range(n):
            if indegree[idx]  == 1:
                q.append(idx)
                seen.add(idx)
        pop_count = len(q)

        while q:

            if len(seen) == n:
                return list(q)
            
            for _ in range(pop_count):
                cur = q.pop()


                for neg in adj[cur]:
                    indegree[neg] -= 1
                    if neg not in seen and indegree[neg] == 1:
                        q.appendleft(neg)
                        seen.add(neg)
            pop_count = len(q)