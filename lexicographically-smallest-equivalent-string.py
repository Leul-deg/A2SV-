class UnionFind:

    def __init__(self):
        
        self.parent = {chr(i) : chr(i) for i in range(97 , 123)}

    
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

            if parent1 < parent2:
                self.parent[parent2] = parent1
            
            else:
                self.parent[parent1] = parent2
        
            


        
    
    def areFamily(self, offspring1 , offspring2 ):

        return self.find_repr(offspring1) == self.find_repr(offspring2)
        
        
        
        
        
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        family = UnionFind()
        idx = 0 

        while idx < len(s1) and idx < len(s2):
            family.union(s1[idx] , s2[idx])
            idx += 1
        
        res =[ family.find_repr(baseStr[idx]) for idx in range(len(baseStr))]
        return "".join(res)