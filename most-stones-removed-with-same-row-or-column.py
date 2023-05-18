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
        if parent2 != parent1:

            if self.size[parent1] > self.size[parent2]:
                self.size[parent1] += self.size[parent2]
                self.parent[parent2] = parent1
            
            else:
                self.size[parent2] += self.size[parent1]
                self.parent[parent1] = parent2
        
    
    def areFamily(self, node1 , node2):

        return self.root(node1) == self.root(node2)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        family = UnionFind(len(stones))
        for i in range(len(stones)):
            x , y = stones[i]
            for j in range(i  + 1 , len(stones)):
                a , b = stones[j]

                if a == x or b == y:
                    family.union( i , j )
        
        parents = set()

        for i in range(len(stones)):
            parents.add(family.root(i))
        
        res = 0

        for num in parents:
            res += family.size[num] -  1
        
        return res