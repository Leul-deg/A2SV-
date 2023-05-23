class UnionFind:

    def __init__(self, size : int):
        self.parent = [i for i in range(size + 1)]
        self.size = [ 1 for _ in range( size + 1)]
    
    def root(self, node):

        hold =  node
        while node != self.parent[node]:
            node = self.parent[node]

        #path compression
        while hold != node:

            temp = self.parent[hold]
            self.parent[hold] = node
            hold = temp
        
        return node
    
    def union(self, node1 , node2):

        #union by size..
        parent1 , parent2 = self.root(node1) , self.root(node2)
        # print(parent1 , parent2 , "parent1 and parent2")
        if parent2 != parent1:

            if parent1 < parent2:
                self.size[parent1] += self.size[parent2]
                self.parent[parent2] = parent1
            
            else:
                self.size[parent2] += self.size[parent1]
                self.parent[parent1] = parent2
            
        
    
    def areFamily(self, node1 , node2):

        return self.root(node1) == self.root(node2)
    
    

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:

        def check(g1 , g2):
            if g1 == g2 :
                return True
            
            for s , e in restrictions:
                p1 , p2 = family.root(s)  , family.root(e)
                if (g1 == p1 and p2 == g2) or( g1 == p2 and g2 == p1):
                    return False
            
            return True

        family = UnionFind(n)
        res = []
        for s , e in requests:
            g1 , g2 = family.root(s) , family.root(e)
            if check(g1 , g2):
                family.union(g1 , g2)
                res.append(True)
            else:
                res.append(False)
        
        return res