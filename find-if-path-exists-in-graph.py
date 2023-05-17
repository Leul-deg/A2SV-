class UnionFind:

    def __init__(self, size : int):
        self.parent = {i : i for i in range(size )}
    
    def find_repr(self, node):

        while node != self.parent[node]:
            node = self.parent[node]
        
        return node
    
    def union(self, bro , sis):

        if self.find_repr(bro) != self.find_repr(sis):

            bro_parent = self.find_repr(bro)
            sis_parent = self.find_repr(sis)

            self.parent[sis_parent]  = bro_parent

    
    def areFamily(self, offspring1 , offspring2 ):

        return self.find_repr(offspring1) == self.find_repr(offspring2)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        family = UnionFind(n)
        for u , v in edges:
            family.union(u  , v)
        
        return family.areFamily(source , destination)