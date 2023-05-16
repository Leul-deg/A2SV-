class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        seen = set()
        d = defaultdict(set)

        for u , v in prerequisites:
            if u != v:
                d[u].add(v)
        
        pre = [set() for _ in range(numCourses)]
        def dfs(node):
            if node in seen:
                # a =  [node] + pre[node]
                return set([node]).union(pre[node])
            
            seen.add(node)
            
            res = set()

            for neg in d[node]:

                res = res.union(dfs(neg))

            pre[node] = pre[node].union(res)

            return res.union( set([node]),  res)
        
        for i in range(numCourses):
            if not pre[i]:
                dfs(i)

        ans = []
        pre = [set(tup) for tup in pre]
        print(pre)
        for u , v in queries:
            ans.append(v in pre[u])
                
        
        return ans