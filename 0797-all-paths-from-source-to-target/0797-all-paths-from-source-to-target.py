class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        last = len(graph) - 1
        seen = set()
        def backtrack(index , path):
            if  index > last:
                return
            if index == last:
                res.append(path)
                return
            for idx in range(len(graph[index])):
                backtrack(graph[index][idx] , path + [graph[index][idx]])
            
        backtrack(0, [0])
        return res
        