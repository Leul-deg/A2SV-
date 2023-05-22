class UnionFind:

    def __init__(self, size : int):
        self.parent = [i for i in range(size + 1)]
        self.size = [ 1 for _ in range( size + 1)]
        self.total = [0 for _ in range(size + 1)]
        self.maximum = 0
    
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
                self.total[parent1] += self.total[parent2]
            
            else:
                self.size[parent2] += self.size[parent1]
                self.parent[parent1] = parent2
                self.total[parent2] += self.total[parent1]
            
        self.maximum = max(self.maximum , self.total[parent1] , self.total[parent2])
        
    
    def areFamily(self, node1 , node2):

        return self.root(node1) == self.root(node2)
    
    def add(self, node, val):
        self.maximum = max(self.maximum ,val )
        self.total[node] = val


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        family = UnionFind(len(nums) + 1)
        res = []
        removeQueries.reverse()
        for q in removeQueries:
            res.append(family.maximum)
            family.add(q, nums[q])
            if family.total[q - 1]:
                family.union(q , q - 1)
            if family.total[q  + 1]:
                family.union(q + 1 , q)
        return reversed(res)