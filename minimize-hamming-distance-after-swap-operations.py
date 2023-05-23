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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        family = UnionFind(len(source))
        for s , e in allowedSwaps:
            
            family.union(s , e)
        
        d = {}
        for idx in range(len(source)):
            p = family.root(idx)
            if p not in d:
                d[p] = defaultdict(int)
            dictt = d[p]
            
            dictt[source[idx]] += 1
        res = 0 
        for idx in range(len(source)):
            p = family.root(idx)
            if not d[p].get(target[idx]) :
                res += 1
            else:
                d[p][target[idx]] -= 1


        


        return res