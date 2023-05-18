class UnionFind:

    def __init__(self, size : int):
        self.parent = [i for i in range(size + 1)]
        self.size = [ 1 for _ in range( size + 1)]
        self.maximum = [_ for _ in range(size + 1)]  
        self.minimum = [float("inf") for _ in range(size + 1)]      
    
    def find_repr(self, node):

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
        parent1 , parent2 = self.find_repr(node1) , self.find_repr(node2)

        if parent2 != parent1:

            if self.size[parent1] > self.size[parent2]:
                self.size[parent1] += self.size[parent2]
                self.parent[parent2] = parent1
                self.maximum[parent1] = max(self.maximum[parent1] , self.maximum[parent2])
                self.minimum[parent1] = min(self.minimum[parent1] , self.minimum[parent2])
            
            else:
                self.size[parent2] += self.size[parent1]
                self.parent[parent1] = parent2
                self.maximum[parent2] = max(self.maximum[parent1] , self.maximum[parent2])
                self.minimum[parent2] = min(self.minimum[parent1] , self.minimum[parent2])


    def areFamily(self, node1 , node2):

        return self.find_repr(node1) == self.find_repr(node2)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        family = UnionFind(n)
        for f , t , c in roads:

            family.union(f , t)
            parent = family.find_repr(f)
            family.minimum[parent] = min(family.minimum[parent] , c)
        
        return family.minimum[family.find_repr(1)]